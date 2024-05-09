import os
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DataCollectionForm

def home_view(request):
    return render(request, 'uchambuzi/home.html')

def data_collection_view(request):
    if request.method == 'POST':
        form = DataCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if file.name.endswith('.csv') or file.name.endswith('.xlsx'):
                try:
                    if file.name.endswith('.csv'):
                        df = pd.read_csv(file)
                    elif file.name.endswith('.xlsx'):
                        df = pd.read_excel(file)
                    
                    # Convert DataFrame to JSON and store in session
                    df_json = df.to_json(orient='records')
                    request.session['uploaded_data'] = df_json
                    
                    # Redirect to the clean_data_view with filename
                    return redirect('clean-data', filename=file.name)
                except Exception as e:
                    error = f"Error reading the file: {e}"
                    return render(request, 'uchambuzi/data_collection.html', {'form': form, 'error': error})
            else:
                error = "Please upload a CSV or Excel file."
                return render(request, 'uchambuzi/data_collection.html', {'form': form, 'error': error})
    else:
        form = DataCollectionForm()
    
    return render(request, 'uchambuzi/data_collection.html', {'form': form})

def clean_data_view(request, filename):
    df_json = request.session.get('uploaded_data')  # Retrieve the DataFrame JSON from session
    if not df_json:
        messages.error(request, 'No data found. Please upload a file first.')
        return redirect('data-collection')
    
    # Convert JSON to DataFrame
    df = pd.read_json(df_json)
    
    cleaning_results = {}
    for column in df.columns:
        column_data = df[column]
        
        # Data cleaning checks
        if column_data.isnull().any():
            cleaning_results[column] = 'Null values found'
        if column_data.dtype == 'object' and column_data.str.contains(' ').any():
            cleaning_results[column] = 'Spaces found in strings'
        if len(column_data.dropna().astype(str).unique()) > 1:
            cleaning_results[column] = 'Different data types found'
    
    # Save cleaned data to a new file
    cleaned_filename = f"{os.path.splitext(filename)[0]}_cleaned.csv"
    cleaned_filepath = os.path.join('media', cleaned_filename)
    df.to_csv(cleaned_filepath, index=False)
    
    # Convert cleaning_results to a dictionary
    cleaning_results_dict = {str(key): str(value) for key, value in cleaning_results.items()}
    
    return render(request, 'uchambuzi/clean_data_results.html', {'cleaning_results': cleaning_results_dict, 'cleaned_filename': cleaned_filename})

def eda_view(request):
    return render(request, 'uchambuzi/eda.html')
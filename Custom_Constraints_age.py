import pandas as pd
from datetime import date
from sdv.constraints import create_custom_constraint_class


def is_valid(column_names, data):
 
  year_list = []
  
  date_column = column_names[0]
  age_column = column_names[1]

  for x in data[date_column]:
    year_list.append(int(x[0:4]))
    
  year = pd.Series(year_list)


  return (date.today().year - year) == data[age_column]


def transform(column_names, data):

  year_list = []
  
  date_column = column_names[0]
  age_column = column_names[1]

  for x in data[date_column]:
    year_list.append(int(x[0:4]))
    
  year = pd.Series(year_list)
  #typical_value = data[age_column].median()
  data[age_column] = data[age_column].mask((date.today().year - year) != data[age_column], 0)
  
  return data


def reverse_transform(column_names, data):

  year_list = []
  
  date_column = column_names[0]
  age_column = column_names[1]

  for x in data[date_column]:
    year_list.append(int(x[0:4]))
    
  year = pd.Series(year_list)
  data[age_column] = data[age_column].mask((date.today().year - year) != data[age_column], (date.today().year - year))
  
  return data




MatchDOBandAge = create_custom_constraint_class(
    is_valid_fn=is_valid,
    transform_fn=transform,
    reverse_transform_fn=reverse_transform
)
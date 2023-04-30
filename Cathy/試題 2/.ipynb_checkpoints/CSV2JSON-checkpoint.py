import pandas as pd
from json import loads, dumps
import sys

def CSV2JSON_function(df):
    trasformation = (df
     .groupby(['member_id','tag_name'],group_keys=True)
     .apply(lambda x: x[['detail_name','detail_value']].to_dict('records'))
     .reset_index() 
     .rename(columns={0:'detail'})
     .groupby(['member_id'],group_keys=True)
     .apply(lambda x: x[['tag_name','detail']].to_dict('records'))
     .reset_index()
     .rename(columns={0:'tags'})
    )
    trasformation['_id'] = trasformation['member_id']
    trasformation = trasformation[["_id","member_id","tags"]]
    return trasformation

if __name__ == "__main__":
    """ main function to transform CSV to JSON"""
    df = pd.read_csv(str(sys.argv[1]))
    trasformation = CSV2JSON_function(df)
    # Serializing json
    json_object = dumps(loads(trasformation.to_json(orient='records')),ensure_ascii=False, indent=4)
 
    # Writing to sample.json
    with open("CSV2JSON.json", "w") as outfile:
        outfile.write(json_object)
    print("Transformation to 'CSV2JSON.json' Success")
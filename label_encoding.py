# 1. Import libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# 2. Create a sample dataset
data = {
    'Name': ['Ali', 'Sara', 'John', 'Sara', 'Ali'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Color': ['Red', 'Blue', 'Green', 'Red', 'Green']
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 3. Label Encoding for Gender (Male=1, Female=0)
label_encoder = LabelEncoder()
df['Gender_Label'] = label_encoder.fit_transform(df['Gender'])

# 4. One-Hot Encoding for Color
one_hot_encoder = OneHotEncoder(sparse_output=False)
color_encoded = one_hot_encoder.fit_transform(df[['Color']])

# Convert One-Hot result to DataFrame
color_df = pd.DataFrame(color_encoded, columns=one_hot_encoder.get_feature_names_out(['Color']))

# 5. Combine everything into final DataFrame
df_final = pd.concat([df, color_df], axis=1)

print("\nEncoded Data:")
print(df_final)
#output
#Original Data:
   Name  Gender  Color
0   Ali    Male    Red
1  Sara  Female   Blue
2  John    Male  Green
3  Sara  Female    Red
4   Ali    Male  Green

#Encoded Data:
   Name  Gender  Color  Gender_Label  Color_Blue  Color_Green  Color_Red
0   Ali    Male    Red             1         0.0          0.0        1.0
1  Sara  Female   Blue             0         1.0          0.0        0.0
2  John    Male  Green             1         0.0          1.0        0.0
3  Sara  Female    Red             0         0.0          0.0        1.0
4   Ali    Male  Green             1         0.0          1.0

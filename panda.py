import pandas as pd

def test_pandas_dataframe():
    # Create a simple DataFrame
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
    df = pd.DataFrame(data)

    # Check if the DataFrame has the correct shape
    assert df.shape == (3, 2), "DataFrame shape is incorrect"

    # Check if the columns are as expected
    assert list(df.columns) == ['Name', 'Age'], "DataFrame columns are incorrect"

    # Check if the data in the DataFrame is as expected
    assert df['Name'].tolist() == ['Alice', 'Bob', 'Charlie'], "DataFrame names are incorrect"
    assert df['Age'].tolist() == [25, 30, 35], "DataFrame ages are incorrect"

    print(df.shape)
    print("All tests passed!")

test_pandas_dataframe()

def test_xlsdata():
    # Create a simple DataFrame
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    df.to_excel(r'C:\\Users\\Mohan\\Documents\\pandata\\test_data.xlsx', index=False)

    # Read the Excel file back into a DataFrame
    df_read = pd.read_excel('C:\\Users\\Mohan\\Documents\\pandata\\test_data.xlsx')

    # Check if the read DataFrame has the correct shape
    assert df_read.shape == (3, 2), "Read DataFrame shape is incorrect"

    # Check if the columns are as expected
    assert list(df_read.columns) == ['Name', 'Age'], "Read DataFrame columns are incorrect"

    # Check if the data in the read DataFrame is as expected
    assert df_read['Name'].tolist() == ['Alice', 'Bob', 'Charlie'], "Read DataFrame names are incorrect"
    assert df_read['Age'].tolist() == [25, 30, 35], "Read DataFrame ages are incorrect"

    print(df_read.shape)
    print("All tests passed for Excel data!")
test_xlsdata()

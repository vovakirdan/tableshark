# TableShark
TableShark is a Python library for working with tables. It provides functionality for parsing, storing, and manipulating
tables in various formats. It also provides a convenient way to handle table headers and cells.

## Installation
You can install TableShark using `pip`:
```shell
pip install tableshark
```
TableShark is a lightweight Python library that simplifies working with tabular data. It provides intuitive classes 
and functions for creating, manipulating, and analyzing tables. With TableLib, you can easily import tables 
from various data sources such as lists, pandas DataFrames, Excel files, CSV files, JSON files, and SQL databases.
You can perform common table operations like adding rows and columns, merging tables, filtering data, and sorting.
The library also offers seamless conversion between tables and popular formats like pandas DataFrames, Excel files,
and CSV files. TableShark's user-friendly API and comprehensive documentation make it a valuable tool for anyone working
with tabular data in Python.

## TableError
`TableError` is a custom exception class defined in this Python library. It is derived from the built-in Exception
class, allowing you to raise and handle specific errors related to table operations.

### Usage
You can use `TableError` to handle exceptional scenarios that may occur during table processing or manipulation.
It provides a straightforward way to identify and handle errors specific to table operations within your codebase.

To raise a `TableError`, you can use the `raise` statement and pass any relevant error message or information as an
argument to the exception. Here's an example:
```python3
from tableshark import TableError

try:
    # Perform table operation
    # ...
    if True:
        raise TableError("An error occurred while performing the table operation.")
    # ...
except TableError as e:
    # Handle the error
    # ...
    pass
```
### Inheriting from `Exception`
Since `TableError` is derived from the `Exception` class, it inherits the basic functionality of exception handling in
Python. This includes capturing traceback information, handling exceptions using `try-except` blocks, and propagating
exceptions up the call stack if not explicitly caught.

### Customization
You can further customize TableError by adding additional attributes or methods as per your requirements.
For example, you can define custom properties to provide more detailed information about the error or include methods
for additional error handling functionality.
```python3
from tableshark import TableError
class TableErrorCustom(TableError):
    def log_error(self):
        # Custom error logging logic
        # ...
        pass
```
Feel free to extend the `TableError` class according to your specific needs.

### Conclusion
TableError is a simple yet powerful custom exception class provided by this library. It enables you to handle and
communicate errors specifically related to table operations in a structured and controlled manner.

## Header
The `Header` class represents the header section of a table in this Python library. It provides functionality for
parsing, storing, and manipulating the columns of the header.

### Usage
To use the `Header` class, you can create an instance by providing the raw header string and the structure type of the
table. The `raw_header` parameter is an optional argument and defaults to an empty string. The `structure` parameter
specifies the structure type of the table and accepts either `'xml'` or `'txt'`. Here's an example of creating
a `Header` object:
```python3
from tableshark import Header
header = Header()
header.columns = ['Column 1', 'Column 2', 'Column 3']
```
Once you have a `Header` object, you can perform various operations on it, such as retrieving columns, setting columns,
iterating over columns, and more.
### Attributes
* `raw_header (str)`: The raw header string provided during initialization.
* `_columns (list[str])`: The parsed columns of the header.
### Methods
* `parse_header(raw_header: str, structure: Literal['xml', 'txt']) -> list[str]`: Parses the raw header based on the 
specified structure type and returns the parsed columns.
* `columns() -> list`: Returns the columns of the header.
* `columns(columns: list)`: Sets the columns of the header.
* `rows()`: Alias for the columns() method.
* `__len__() -> int`: Returns the number of columns in the header.
* `__iter__() -> Iterator[str]`: Returns an iterator over the columns of the header.
* `__getitem__(item: Union[str, int, Tuple[int], Tuple[int, int]]) -> Union[str, List[str]]`: Retrieves a column based 
on its name or index. It can also retrieve a column based on 2-dimensional coordinates or a slice object.
* `__setitem__(key: Union[str, int], value: str)`: Sets the value of a column based on its name or index.
* `__repr__() -> str`: Returns a string representation of the header.
* `__add__(other: Union[str, List[str], Tuple[str], Header]) -> Header`: Concatenates the header with another header or
a column. Returns a new Header object with the concatenated columns.
* `__iadd__(other: Union[str, List[str], Tuple[str], Header])`: Concatenates the header with another header or a column 
in-place.
### Example
```python3
from tableshark import Header

raw_header =\
'''
+-----------------+-----------------+-----------------+
|     Column 1    |     Column 2    |     Column 3    |
+-----------------+-----------------+-----------------+
'''

# Create a Header object
header = Header(raw_header, structure='txt')

# Retrieve columns
columns = header.columns

# Set columns
new_columns = ['Column A', 'Column B', 'Column C']
header.columns = new_columns

# Iterate over columns
for column in header:
    print(column)

# Get the number of columns
num_columns = len(header)

# Get a column by name or index
column_1 = header['Column A']
column_2 = header[1]

# Set the value of a column
header['Column B'] = 'New Value'

# Concatenate headers
other_header = Header('Another Header')
concatenated_header = header + other_header

# In-place concatenation
header += 'Extra Column'
```
### Conclusion
The `Header` class provides a convenient way to handle the header section of a table. You can parse, store, and 
manipulate columns with ease using the methods provided by this class. Incorporate the `Header` class into your table
processing workflows to efficiently work with table headers.

## Cell
The `Cell` class represents a cell in a table. It encapsulates a value and provides various methods and properties for
working with the cell.

### Usage
To create a `Cell` object, you can initialize it with a value. The value can be of any type. Here's an example of 
creating a `Cell` object:
```python3
from tableshark import Cell
cell = Cell('Cell Value')
```
Once you have a `Cell` object, you can perform various operations on it, such as retrieving the value, setting the
value, getting and setting the name, changing the type, and more.
### Attributes
* `_value (Any)`: The value of the cell.
* `_name (str)`: The name of the cell.
* `_type (str)`: The type of the cell.
### Methods
* `name() -> str`: Returns the name of the cell.
* `name(new_name: str)`: Sets the name of the cell.
* `value() -> Any`: Returns the value stored in the cell.
* `value(new_value)`: Sets the value of the cell.
* `type() -> type`: Returns the type of the value.
* `new_type(new: Callable)`: Changes the type of the value by applying a callable function.
* `__str__() -> str`: Returns a string representation of the cell.
* `__repr__() -> str`: Returns a string representation of the cell that can be used to recreate the cell object.
* `__len__() -> int`: Returns the length of the value stored in the cell.
* `__eq__(other)` -> bool: Checks if the value stored in the cell is equal to the provided value.
* `__setattr__(key, value)`: Overrides the default __setattr__ method to allow setting attributes.
### Example
```python3
from tableshark import Cell
# Create a Cell object
cell = Cell('value')

# Get the name of the cell
name = cell.name()

# Set the name of the cell
cell.name = 'Cell 1'

# Get the value of the cell
value = cell.value()

# Set the value of the cell
cell.value = 'new_value'

# Get the type of the value
cell_type = cell.type()

# Change the type of the value
cell.new_type(int)

# Get a string representation of the cell
cell_str = str(cell)

# Get a representation of the cell that can be used to recreate the object
cell_repr = repr(cell)

# Get the length of the value stored in the cell
value_length = len(cell)

# Check if the value stored in the cell is equal to another value
is_equal = cell == 'other_value'

# Set an attribute of the cell
cell.attribute = 'attribute_value'
```
### Conclusion
The `Cell` class provides a flexible way to work with individual cells in a table. You can access and modify the value,
name, and type of a cell using the methods and properties offered by this class. Incorporate the `Cell` class into your
table processing workflows to effectively handle table cells.

## Vector, Row, and Column
The `Vector`, `Row`, and `Column` classes represent a vector, row, and column in a table, respectively. They encapsulate
a list of cells and provide various methods and properties for working with the vector, row, or column.

### Vector (Abstract Base Class)
The `Vector` class is an abstract base class (ABC) that provides a common interface and functionality for vectors. 
It contains a collection of `Cell` objects and defines various methods and properties to work with these cells.

Key methods and properties:

* `__init__(*cells: Cell | Any)`: Initializes a Vector object with a variable number of Cell objects or values. If a 
value is provided instead of a Cell, it will be automatically converted into a Cell object.
* `__getitem__(key: str | int) -> Any`: Retrieves the value of a cell in the vector by cell name or index.
* `__setitem__(key, value)`: Sets the value of a cell in the vector by index.
* `cell(i) -> Cell`: Returns the Cell object at the specified index.
* `cells() -> list[Cell]`: Returns a list of Cell objects in the vector.
* `to_dict() -> dict`: Converts the vector into a dictionary, where keys are cell names (or indices) and values are cell
values.
* `__eq__(other) -> bool`: Checks if two vectors are equal by comparing their cells.
* `__iter__() -> Iterator[Cell]`: Allows iteration over the cells in the vector.
* `df() -> pd.DataFrame (abstract)`: Converts the vector into a pandas DataFrame.
* `__iadd__(other)`: Adds a Cell or Vector object to the vector in-place.
* `__add__(other: Cell | Vector) -> Vector`: Adds a Cell or Vector object to the vector and returns a new Vector object.
* `from_raw(value: Iterable[Any]) -> Vector`: Initializes the vector from an iterable of values.
* `apply(func: Callable[[Cell, Any], Cell], *args: Any) -> Vector`: Applies a function to each cell in the vector.
### Row (Subclass of Vector)
The Row class is a subclass of Vector and represents a row of cells in a table-like structure.

#### Initialization
To create a `Row` object, you can pass a variable number of arguments representing the cells of the row. Each
argument can be an instance of the `Cell` class or any other value. If a non-`Cell` value is provided, it will be
automatically converted into a `Cell` object. Here's an example of creating a Row object:
```python3
from tableshark import Row, Cell
row = Row(Cell(1), Cell(2), Cell(3))
# or alternatively
row_1 = Row(1, 2, 3)  # 1, 2, and 3 will be converted into Cell objects
```

#### Additional methods:

* `_str() -> str`: Returns a string representation of the row.
* `df() -> pd.DataFrame`: Converts the row into a pandas DataFrame.
* `_T() -> Column`: Transposes the row into a Column object.
### Column (Subclass of Vector)
The Column class is a subclass of Vector and represents a column of cells in a table-like structure.

#### Initialization
To create a `Column` object, you can pass a variable number of arguments representing the cells of the column.
Each argument can be an instance of the `Cell` class or any other value. If a non-`Cell` value is provided, it will be
automatically converted into a `Cell` object.
```python3
from tableshark import Column, Cell
column = Column(Cell(1), Cell(2), Cell(3))
# or alternatively
column_1 = Column(1, 2, 3)  # 1, 2, and 3 will be converted into Cell objects
```

#### Additional methods:

* `_str() -> str`: Returns a string representation of the column.
* `df() -> pd.DataFrame`: Converts the column into a pandas DataFrame.
* `_T() -> Row`: Transposes the column into a Row object.
These classes provide a convenient and flexible way to work with vectors, rows, and columns of cells in tabular
data structures. They offer methods for accessing, manipulating, and converting the data represented by the vectors.

## Body
The Body class represents the body of a table, consisting of rows and columns.

### Usage
To create an instance of the `Body` class, you need to provide the raw body content of the table as a string, the
structure type ('xml' or 'txt'), and an optional iterable of `Row` objects. Here's an example of creating a Body object:
```python3
from tableshark import Body
raw_body = \
"""
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
"""
body = Body(raw_body, structure='txt')
```
Or alternatively, you can create a Body object from an iterable of Row objects:
```python3
from tableshark import Body, Row
rows = [Row(1, 2, 3), Row(4, 5, 6)]
body = Body(rows=rows)
```
You can access the attributes and methods of the Body object to work with the body content of the table.
### Attributes
The Body class has the following attributes:

* `raw_body (str)`: The raw body content of the table.
* `structure (Literal['xml', 'txt'])`: The structure type of the body content.
* `rows (list[Row])`: The list of rows in the body.
* `number_of_columns (int)`: The number of columns in the body.
### Methods
The Body class provides the following methods:

* `parse_body(raw_body: str = '', structure: Literal['xml', 'txt'] = 'txt') -> list[Row]`: Parse the raw body content
and return a list of Row objects.
### Example
Here's an example of how to use the Body class:

```python3
from tableshark import Body
raw_body = \
"""
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
"""
body = Body(raw_body, structure='txt')
# Example: Accessing the rows
rows = body.rows

# Example: Accessing the number of columns
number_of_columns = body.number_of_columns

# Example: Iterating over the rows
for row in body:
    print(row)
# Output:
# Row(Cell(1), Cell(2), Cell(3))
# Row(Cell(4), Cell(5), Cell(6))
```
### Conclusion
The `Body` class provides a convenient way to represent and work with the body content of a table. 
It allows you to parse the raw body content, access rows and columns, and iterate over the rows. Incorporate
the `Body` class into your table-related projects to handle table bodies with ease.

## Table
The Table class represents a table structure.

### Usage
You can create an instance of the Table class by providing the table structure as a string, or by specifying the header
and body separately.

```python3
from tableshark import Table
table_structure = \
"""
+---+---+---+
| a | b | c |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
"""
table = Table(stream=table_structure, structure='txt')
```
or
```python3
from tableshark import Table, Header, Body, Row
header = Header()
header.columns = ['Column 1', 'Column 2', 'Column 3']
body = Body(rows=Row(['row1', 'row2', 'row3']))
table = Table(header=header, body=body)
```
Access the attributes, properties, and methods of the Table object to work with the table structure.

```python3
from tableshark import Table
table = Table()  # imagine that we have already created a Table object
# Example: Accessing the header and body
header = table.header
body = table.body

# Example: Accessing a specific column
column = table.column(2)

# Example: Accessing a specific row
row = table.row(1)

# Example: Accessing a specific cell
cell = table.cells(2, 3)
```
### Attributes
The Table class has the following attributes:

* `header (Header)`: The header of the table.
* `body (Body)`: The body of the table.
### Properties
The Table class provides the following properties:

* `header (Header)`: The getter and setter for the table's header.
* `body (Body)`: The getter and setter for the table's body.
### Methods
The Table class provides the following methods:

* `column(col: int | str) -> Column`: Retrieve a full column of the table.
* `row(row: int) -> Row`: Retrieve a specific row of the table.
* `cells(row: int, column: int) -> Cell`: Retrieve a specific cell of the table.
### Magic Methods
The Table class implements the following magic methods:

* `__getitem__(item: int | str) -> Row | Column`: Retrieve a specific row or column of the table.
* `__iter__() -> Iterator[Row]`: Iterate over the rows of the table.
* `__len__() -> int`: Return the number of rows in the table.
* `__str__() -> str`: Return a string representation of the table.
* `__repr__() -> str`: Return a string representation of the table.

Because of the magic methods, you can use the Table object as if it were a list of rows. For example, you can iterate
over the rows of the table, access a specific row, or get the number of rows in the table.
    
```python3
from tableshark import Table, Body, Row

table = Table()
table.header = ['Column 1', 'Column 2', 'Column 3']
table.body = Body(rows=[Row(1, 2, 3), Row(4, 5, 6)])
# Example: Iterating over the rows
for row in table:
    print(row)
# Output:
# Row(Cell(1), Cell(2), Cell(3))
# Row(Cell(4), Cell(5), Cell(6))

# Example: Accessing a specific row
row = table[1]
# or alternatively
row = table.row(1)
print(row)
# Output:
# Row(Cell(4), Cell(5), Cell(6))

# Example: Getting the number of rows
number_of_rows = len(table)

# Example: Getting a specific cell
cell = table[1][2]
# or alternatively
cell = table.cells(1, 2)
print(cell)
# Output:
# Cell(6)

# Example: Getting a specific column
column = table['Column 2']
# or alternatively
column = table.column(2)
print(column)
# Output:
# Column(Cell(2), Cell(5))

# Also you can set the value of a specific cell
table[1][2] = 7
```

### Conclusion
The Table class provides a convenient way to represent and manipulate table structures. It allows you to access
the header, body, rows, columns, and individual cells of the table. Incorporate the Table class into your projects
to handle table-related operations with ease.

## Schema
The Schema class represents a collection of tables.

### Usage
To use the Schema class, follow these steps:

```python3
from tableshark import Schema, Table
# 1. Create an instance of the Schema class by providing the tables as arguments.
schema = Schema(Table(), Table())
# 2. Access the tables within the schema using iteration or indexing.
for table in schema:
    print(table)
# or
table = schema[0]
# 3. Add tables to the schema using the addition operator.
new_table = Table()
schema = schema + new_table
```
### Methods
The Schema class provides the following methods:

* `from_excel(file_path, sheet_names=None) -> Schema`: Create a Schema instance from an Excel file.
* `from_csv(file_path, delimiter=',') -> Schema`: Create a Schema instance from a CSV file.
* `from_sql(executor, table_names=None) -> Schema`: Create a Schema instance from a SQL database.
* `from_json(file_path) -> Schema`: Create a Schema instance from a JSON file.
* `from_io(stream, type_='excel', **kwargs) -> Schema`: Create a Schema instance from a stream (e.g., BytesIO) of
a specific type, such as Excel.
### Magic Methods
The Schema class implements the following magic methods:

* `__iter__() -> Iterator[Table]`: Iterate over the tables in the schema.
* `__add__(other: Table) -> Schema`: Add a table to the schema.
* `__getitem__(item) -> Table`: Get a specific table from the schema using indexing.
* `__len__() -> int`: Get the number of tables in the schema.

#### String Representation
The Schema class provides a string representation of the schema using the `__str__()` and `__repr__()` methods.

* `__str__()`: Returns a string representation of the schema.
* `__repr__()`: Returns a string representation that can be used to recreate the schema.
### Conclusion
The `Schema` class allows you to organize and work with a collection of tables. It provides methods to create a 
schema from various sources such as Excel files, CSV files, SQL databases, and JSON files. You can iterate over
the tables, add new tables, and access specific tables within the schema. Use the `Schema` class to manage and 
manipulate multiple tables efficiently in your projects.
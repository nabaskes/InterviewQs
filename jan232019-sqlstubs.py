# -- Question 84 - In SQL, 0 = 0?

# -- In SQL, what will be the result of the below query?

# -- select case when 0 = 0 then 'Yes' else 'No' end as Result;

# -- Upgrade to premium to receive in-depth solutions to each problem.

'''
0 = 0 in most if not all versions of SQL.  This is generally used when we are generating queries in a different program.  If you want different conditions depending on other criterion, you would do something like
'''

query = '''SELECT * FROM MyTable
WHERE 1 = 1'''

if use_condition_1p():
    query += " AND Val1 is not Null"
if use_condition_2p():
    query += f" AND Val2 = '{val2_parameter}'"

'''
and so on.  This is cleaner than having to have logic in all but the first
possible condition in order to check whether the "WHERE" statement has already been added, etc, '''

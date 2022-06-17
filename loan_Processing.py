import lms_master_data as md
#print(md.master_data)
#print("******************************************************************************************************")
cust_name="ABC"
cust_credit_score=190
cust_requested_loan=20909
print("Starting Loan Processing")
for c1 in md.master_data:
    #print(c1)
    if cust_credit_score>=c1["cs_start"] and  cust_credit_score<=c1["cs_End"] \
    and cust_requested_loan>=c1["Loan_amount_start"] and cust_requested_loan<=c1["Loan_amount_End"]:
        print("Approved")
        print(c1["interest"])
        print(c1["duration"])            
print("Done Loan Processing")

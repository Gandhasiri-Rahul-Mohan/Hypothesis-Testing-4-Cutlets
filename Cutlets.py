import pandas as pd
cutlets = pd.read_csv("D:\\DS\\books\\ASSIGNMENTS\\Hypothesis testing\\Cutlets.csv")
cutlets

cutlets.shape

# MEAN X
cutlets["Unit A"].mean()
cutlets["Unit B"].mean()

# TWO SAMPLE TEST
from scipy import stats as twosample
zscale, pval = twosample.ttest_ind(cutlets["Unit A"], cutlets["Unit B"])

print("Z_Calculated value: ", zscale)
print("P_value: ", pval)

alpha = 0.05

if pval<alpha:
    print("Ho is Rejected and H1 is Accepted")
else:
    print("Ho is Accepted and H1 is Rejected")
    
# CONCLUSION
"""
In this Ho is Accepted and H1 is Rejected then there is no significant 
difference between those two units and no difference in diameter of the cutlet.
"""
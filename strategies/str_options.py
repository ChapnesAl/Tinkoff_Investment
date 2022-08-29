
""" Market One Day More"""

m1_m = "gf_copy.iloc[ind[i], 2] > gf_copy.iloc[ind[i] - 1, 2]"
m1_m_m = "gf_copy.iloc[ind[i], 2] > gf_copy.iloc[ind[i] - 1, 2] > gf_copy.iloc[ind[i] - 2, 2]"
m1_m_m_m = "gf_copy.iloc[ind[i], 2] > gf_copy.iloc[ind[i] - 1, 2] > gf_copy.iloc[ind[i] - 2, 2] > gf_copy.iloc[ind[i] - 3, 2]"
m1_m_m_m_m = "gf_copy.iloc[ind[i], 2] > gf_copy.iloc[ind[i] - 1, 2] > gf_copy.iloc[ind[i] - 2, 2] > gf_copy.iloc[ind[i] - 3, 2] > gf_copy.iloc[ind[i] - 4, 2]"
p1_m1 = (m1_m, m1_m_m, m1_m_m_m, m1_m_m_m_m)

m1_m05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 0.5)"
m1_m1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1)"
m1_m15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5)"
m1_m2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 2)"
p2_m1 = (m1_m05, m1_m1, m1_m15, m1_m2)

m1_m05_m05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 0.5)  > (gf_copy.iloc[ind[i] - 2, 2] + 0.5)"
m1_m1_m1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1)  > (gf_copy.iloc[ind[i] - 2, 2] + 1)"
m1_m15_m15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5)  > (gf_copy.iloc[ind[i] - 2, 2] + 1.5)"
m1_m2_m2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 2)  > (gf_copy.iloc[ind[i] - 2, 2] + 2)"
p3_m1 = (m1_m05_m05, m1_m1_m1, m1_m15_m15, m1_m2_m2)

m1_m_05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 0.5)"
m1_m_1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1)"
m1_m_15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1.5)"
m1_m_2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 2)"
p4_m1 = (m1_m_05, m1_m_1, m1_m15, m1_m_2)



""" Market One Day Less"""

m1_l = "gf_copy.iloc[ind[i], 2] < gf_copy.iloc[ind[i] - 1, 2]"
m1_l_l = "gf_copy.iloc[ind[i], 2] < gf_copy.iloc[ind[i] - 1, 2] < gf_copy.iloc[ind[i] - 2, 2]"
m1_l_l_l = "gf_copy.iloc[ind[i], 2] < gf_copy.iloc[ind[i] - 1, 2] < gf_copy.iloc[ind[i] - 2, 2] < gf_copy.iloc[ind[i] - 3, 2]"
m1_l_l_l_l = "gf_copy.iloc[ind[i], 2] < gf_copy.iloc[ind[i] - 1, 2] < gf_copy.iloc[ind[i] - 2, 2] < gf_copy.iloc[ind[i] - 3, 2] < gf_copy.iloc[ind[i] - 4, 2]"


m1_l05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 0.5)"
m1_l1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1)"
m1_l15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5)"
m1_l2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 2)"

m1_l_05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 0.5)"
m1_l_1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1)"
m1_l_15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1.5)"
m1_l_2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 2)"

if __name__ == '__main__':
    print(m1_m)
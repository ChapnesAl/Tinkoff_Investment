
""" Market One Day More"""

m1_m = "gf_copy.iloc[ind[i], 2] > gf_copy.iloc[ind[i] - 1, 2]"
m1_m_m = "gf_copy.iloc[ind[i], 2] > gf_copy.iloc[ind[i] - 1, 2] > gf_copy.iloc[ind[i] - 2, 2]"
m1_m_m_m = "gf_copy.iloc[ind[i], 2] > gf_copy.iloc[ind[i] - 1, 2] > gf_copy.iloc[ind[i] - 2, 2] > gf_copy.iloc[ind[i] - 3, 2]"
m1_m_m_m_m = "gf_copy.iloc[ind[i], 2] > gf_copy.iloc[ind[i] - 1, 2] > gf_copy.iloc[ind[i] - 2, 2] > gf_copy.iloc[ind[i] - 3, 2] > gf_copy.iloc[ind[i] - 4, 2]"
m1_m05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 0.5)"
m1_m1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1)"
m1_m15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5)"
m1_m2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 2)"
m1_m25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 2.5)"
m1_m3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 3)"
m1_m35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 3.5)"
m1_m4 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 4)"
m1_m_05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 0.5)"
m1_m_1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1)"
m1_m_15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1.5)"
m1_m_2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 2)"
m1_m_25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 2.5)"
m1_m_3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 3)"
m1_m_35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 3.5)"
m1_m_4 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 4)"
p1_mr = (m1_m, m1_m_m, m1_m_m_m, m1_m_m_m_m, m1_m05, m1_m1, m1_m15, m1_m2, m1_m25, m1_m3, m1_m35, m1_m4, m1_m_05, m1_m_1, m1_m_15, m1_m_2, m1_m_25, m1_m_3, m1_m_35, m1_m_4)


m1_m05_m05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 0.5)  > (gf_copy.iloc[ind[i] - 2, 2] + 0.5)"
m1_m1_m1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1)  > (gf_copy.iloc[ind[i] - 2, 2] + 1)"
m1_m15_m15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5)  > (gf_copy.iloc[ind[i] - 2, 2] + 1.5)"
m1_m2_m2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 2)  > (gf_copy.iloc[ind[i] - 2, 2] + 2)"
m1_m05_m_05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 0.5)  > (gf_copy.iloc[ind[i] - 2, 2] - 0.5)"
m1_m1_m_1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1)  > (gf_copy.iloc[ind[i] - 2, 2] - 1)"
m1_m2_m_2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 2)  > (gf_copy.iloc[ind[i] - 2, 2] - 2)"
p2_mr = (m1_m05_m05, m1_m1_m1, m1_m15_m15, m1_m2_m2, m1_m05_m_05, m1_m1_m_1, m1_m2_m_2 )

m1_m15_m15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] + 1.5)"
m1_m15_m2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] + 2)"
m1_m15_m1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] + 1)"
m1_m15_m05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] + 0.5)"
m1_m15_m_15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] - 1.5)"
m1_m15_m_05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] - 0.5)"
m1_m15_m_1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] - 1)"
m1_m15_m_2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] - 2)"
p3_mr = (m1_m15_m15, m1_m15_m2, m1_m15_m1, m1_m15_m05, m1_m15_m_15, m1_m15_m_05, m1_m15_m_1, m1_m15_m_2)


m1_m15_a_m1m0 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 0"
m1_m15_a_m1m05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 0.5"
m1_m15_a_m1m1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 1"
m1_m15_a_m1m15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 1.5"
m1_m15_a_m1m2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 2"
m1_m15_a_m1m25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 2.5"
m1_m15_a_m1m3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 3"
m1_m15_a_m1m35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 3.5"
m1_m15_a_m1m4 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 4"
m1_m15_a_m1l0 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 0"
m1_m15_a_m1l05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 0.5"
m1_m15_a_m1l1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 1"
m1_m15_a_m1l15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 1.5"
m1_m15_a_m1l2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 2"
m1_m15_a_m1l25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 2.5"
m1_m15_a_m1l3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 3"
m1_m15_a_m1l35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 3.5"
m1_m15_a_m1l4 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 4"
p4_mr = (m1_m15_a_m1m0, m1_m15_a_m1m05, m1_m15_a_m1m1, m1_m15_a_m1m15, m1_m15_a_m1m2, m1_m15_a_m1m25, m1_m15_a_m1m3, m1_m15_a_m1m35, m1_m15_a_m1m4,
         m1_m15_a_m1l0, m1_m15_a_m1l05, m1_m15_a_m1l1, m1_m15_a_m1l15, m1_m15_a_m1l2, m1_m15_a_m1l25,  m1_m15_a_m1l3, m1_m15_a_m1l35, m1_m15_a_m1l4)


m1_m1_a_m1m0 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 0"
m1_m1_a_m1m05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 0.5"
m1_m1_a_m1m1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 1"
m1_m1_a_m1m15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 1.5"
m1_m1_a_m1m2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 2"
m1_m1_a_m1m25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 2.5"
m1_m1_a_m1m3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 3"
m1_m1_a_m1m35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 3.5"
m1_m1_a_m1m4 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 4"
m1_m1_a_m1m45 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 4.5"
m1_m1_a_m1l0 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 0"
m1_m1_a_m1l05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 0.5"
m1_m1_a_m1l1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 1"
m1_m1_a_m1l15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 1.5"
m1_m1_a_m1l2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 2"
m1_m1_a_m1l25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 2.5"
m1_m1_a_m1l3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 3"
m1_m1_a_m1l35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 3.5"
m1_m1_a_m1l4 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 4"
m1_m1_a_m1l45 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 4.5"
p5_mr = (m1_m1_a_m1m0, m1_m1_a_m1m05, m1_m1_a_m1m1, m1_m1_a_m1m15, m1_m1_a_m1m2, m1_m1_a_m1m25, m1_m1_a_m1m3, m1_m1_a_m1m35, m1_m1_a_m1m4, m1_m1_a_m1m45,
         m1_m1_a_m1l0, m1_m1_a_m1l05, m1_m1_a_m1l1, m1_m1_a_m1l15, m1_m1_a_m1l2, m1_m1_a_m1l25, m1_m1_a_m1l3, m1_m1_a_m1l35, m1_m1_a_m1l4, m1_m1_a_m1l45)


m1_m_1_a_m1m0 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 0"
m1_m_1_a_m1m05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 0.5"
m1_m_1_a_m1m1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 1"
m1_m_1_a_m1m15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 1.5"
m1_m_1_a_m1m2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 2"
m1_m_1_a_m1m25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 2.5"
m1_m_1_a_m1m3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 3"
m1_m_1_a_m1m35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 3.5"
m1_m_1_a_m1m4 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 4"
m1_m_1_a_m1m45 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 4.5"
m1_m_1_a_m1l0 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 0"
m1_m_1_a_m1l05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 0.5"
m1_m_1_a_m1l1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 1"
m1_m_1_a_m1l15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 1.5"
m1_m_1_a_m1l2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 2"
m1_m_1_a_m1l25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 2"
m1_m_1_a_m1l3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 2"
m1_m_1_a_m1l35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 2"
m1_m_1_a_m1l4 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 2"
m1_m_1_a_m1l45 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 2"

p6_mr = (m1_m_1_a_m1m0, m1_m_1_a_m1m05, m1_m_1_a_m1m1, m1_m_1_a_m1m15, m1_m_1_a_m1m2, m1_m_1_a_m1m25, m1_m_1_a_m1m3, m1_m_1_a_m1m35, m1_m_1_a_m1m4, m1_m_1_a_m1m45,
         m1_m_1_a_m1l0, m1_m_1_a_m1l05, m1_m_1_a_m1l1, m1_m_1_a_m1l15, m1_m_1_a_m1l2, m1_m_1_a_m1l25, m1_m_1_a_m1l3, m1_m_1_a_m1l35, m1_m_1_a_m1l4, m1_m_1_a_m1l45)


mrAM_MmrB15_a_mrAM1_a_mrBM0 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 0"
mrAM_MmrB15_a_mrAM1_a_mrBM05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 0.5"
mrAM_MmrB15_a_mrAM1_a_mrBM1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 1"
mrAM_MmrB15_a_mrAM1_a_mrBM15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 1.5"
mrAM_MmrB15_a_mrAM1_a_mrBM2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 2"
mrAM_MmrB15_a_mrAM1_a_mrBM25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 2.5"
mrAM_MmrB15_a_mrAM1_a_mrBM3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 3"
mrAM_MmrB15_a_mrAM1_a_mrBM35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 3.5"
mrAM_MmrB15_a_mrAM1_a_mrBL0 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 0"
mrAM_MmrB15_a_mrAM1_a_mrBL05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 0.5"
mrAM_MmrB15_a_mrAM1_a_mrBL1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 1"
mrAM_MmrB15_a_mrAM1_a_mrBL15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 1.5"
mrAM_MmrB15_a_mrAM1_a_mrBL2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 2"
mrAM_MmrB15_a_mrAM1_a_mrBL25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 2.5"
mrAM_MmrB15_a_mrAM1_a_mrBL3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 3"
mrAM_MmrB15_a_mrAM1_a_mrBL35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 3.5"
p7_mr = (mrAM_MmrB15_a_mrAM1_a_mrBM0, mrAM_MmrB15_a_mrAM1_a_mrBM05, mrAM_MmrB15_a_mrAM1_a_mrBM1, mrAM_MmrB15_a_mrAM1_a_mrBM15, mrAM_MmrB15_a_mrAM1_a_mrBM2,
         mrAM_MmrB15_a_mrAM1_a_mrBM25, mrAM_MmrB15_a_mrAM1_a_mrBM3, mrAM_MmrB15_a_mrAM1_a_mrBM35, mrAM_MmrB15_a_mrAM1_a_mrBL0, mrAM_MmrB15_a_mrAM1_a_mrBL05, mrAM_MmrB15_a_mrAM1_a_mrBL1,
         mrAM_MmrB15_a_mrAM1_a_mrBL15, mrAM_MmrB15_a_mrAM1_a_mrBL2, mrAM_MmrB15_a_mrAM1_a_mrBL25, mrAM_MmrB15_a_mrAM1_a_mrBL3, mrAM_MmrB15_a_mrAM1_a_mrBL35)


m1_m1_a_m1m_05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > -0.5"
m1_m1_a_m1m_1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > -1"
m1_m1_a_m1m_15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > -1.5"
m1_m1_a_m1m_2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > -2"
m1_m1_a_m1m_25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > -2.5"
m1_m1_a_m1m_3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > -3"
m1_m1_a_m1m_35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > -3.5"
m1_m1_a_m1m_4 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > -4"
m1_m1_a_m1l_05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < -0.5"
m1_m1_a_m1l_1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < -1"
m1_m1_a_m1l_15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < -1.5"
m1_m1_a_m1l_2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < -2"
m1_m1_a_m1l_25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < -2.5"
m1_m1_a_m1l_3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < -3"
m1_m1_a_m1l_35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < -3.5"
m1_m1_a_m1l_4 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < -4"
p8_mr = (m1_m1_a_m1m_05, m1_m1_a_m1m_1, m1_m1_a_m1m_15, m1_m1_a_m1m_2, m1_m1_a_m1m_25, m1_m1_a_m1m_3, m1_m1_a_m1m_35, m1_m1_a_m1m_4,
         m1_m1_a_m1l_05, m1_m1_a_m1l_1, m1_m1_a_m1l_15, m1_m1_a_m1l_2, m1_m1_a_m1l_25, m1_m1_a_m1l_3, m1_m1_a_m1l_35, m1_m1_a_m1l_4)


m1_m_1_a_m1m_05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > - 0.5"
m1_m_1_a_m1m_1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > - 1"
m1_m_1_a_m1m_15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > - 1.5"
m1_m_1_a_m1m_2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > - 2"
m1_m_1_a_m1m_25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > - 2.5"
m1_m_1_a_m1m_3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > - 3"
m1_m_1_a_m1m_35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > - 3.5"
m1_m_1_a_m1m_4 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > - 4"
m1_m_1_a_m1l_05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < - 0.5"
m1_m_1_a_m1l_1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < - 1"
m1_m_1_a_m1l_15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < - 1.5"
m1_m_1_a_m1l_2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] <  - 2"
m1_m_1_a_m1l_25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < - 2.5"
m1_m_1_a_m1l_3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < - 3"
m1_m_1_a_m1l_35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < - 3.5"
m1_m_1_a_m1l_4 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < - 4"

p9_mr = (m1_m_1_a_m1m_05, m1_m_1_a_m1m_1, m1_m_1_a_m1m_15, m1_m_1_a_m1m_2, m1_m_1_a_m1m_25, m1_m_1_a_m1m_3, m1_m_1_a_m1m_35, m1_m_1_a_m1m_4,
         m1_m_1_a_m1l_05, m1_m_1_a_m1l_1, m1_m_1_a_m1l_15, m1_m_1_a_m1l_2, m1_m_1_a_m1l_25, m1_m_1_a_m1l_3, m1_m_1_a_m1l_35, m1_m_1_a_m1l_4)



mrAM_MmrB15_a_mrAM1_a_mrBM_05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -0.5"
mrAM_MmrB15_a_mrAM1_a_mrBM_1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -1"
mrAM_MmrB15_a_mrAM1_a_mrBM_15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -1.5"
mrAM_MmrB15_a_mrAM1_a_mrBM_2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -2"
mrAM_MmrB15_a_mrAM1_a_mrBM_25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -2.5"
mrAM_MmrB15_a_mrAM1_a_mrBM_3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -3"
mrAM_MmrB15_a_mrAM1_a_mrBM_35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -3.5"
mrAM_MmrB15_a_mrAM1_a_mrBL_05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -0.5"
mrAM_MmrB15_a_mrAM1_a_mrBL_1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -1"
mrAM_MmrB15_a_mrAM1_a_mrBL_15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -1.5"
mrAM_MmrB15_a_mrAM1_a_mrBL_2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -2"
mrAM_MmrB15_a_mrAM1_a_mrBL_25 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -2.5"
mrAM_MmrB15_a_mrAM1_a_mrBL_3 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -3"
mrAM_MmrB15_a_mrAM1_a_mrBL_35 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -3.5"
p10_mr = (mrAM_MmrB15_a_mrAM1_a_mrBM_05, mrAM_MmrB15_a_mrAM1_a_mrBM_1, mrAM_MmrB15_a_mrAM1_a_mrBM_15, mrAM_MmrB15_a_mrAM1_a_mrBM_2, mrAM_MmrB15_a_mrAM1_a_mrBM_25, mrAM_MmrB15_a_mrAM1_a_mrBM_3,
          mrAM_MmrB15_a_mrAM1_a_mrBM_35, mrAM_MmrB15_a_mrAM1_a_mrBL_05, mrAM_MmrB15_a_mrAM1_a_mrBL_1, mrAM_MmrB15_a_mrAM1_a_mrBL_15, mrAM_MmrB15_a_mrAM1_a_mrBL_2, mrAM_MmrB15_a_mrAM1_a_mrBL_25,
          mrAM_MmrB15_a_mrAM1_a_mrBL_3, mrAM_MmrB15_a_mrAM1_a_mrBL_35)

""" Market One Day Less"""

m1_l = "gf_copy.iloc[ind[i], 2] < gf_copy.iloc[ind[i] - 1, 2]"
m1_l_l = "gf_copy.iloc[ind[i], 2] < gf_copy.iloc[ind[i] - 1, 2] < gf_copy.iloc[ind[i] - 2, 2]"
m1_l_l_l = "gf_copy.iloc[ind[i], 2] < gf_copy.iloc[ind[i] - 1, 2] < gf_copy.iloc[ind[i] - 2, 2] < gf_copy.iloc[ind[i] - 3, 2]"
m1_l_l_l_l = "gf_copy.iloc[ind[i], 2] < gf_copy.iloc[ind[i] - 1, 2] < gf_copy.iloc[ind[i] - 2, 2] < gf_copy.iloc[ind[i] - 3, 2] < gf_copy.iloc[ind[i] - 4, 2]"
m1_l05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 0.5)"
m1_l1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1)"
m1_l15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5)"
m1_l2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 2)"
m1_l25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 2.5)"
m1_l3 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 3)"
m1_l35 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 3.5)"
m1_l4 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 4)"
m1_l_05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 0.5)"
m1_l_1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1)"
m1_l_15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1.5)"
m1_l_2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 2)"
m1_l_25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 2.5)"
m1_l_3 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 3)"
m1_l_35 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 3.5)"
m1_l_4 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 4)"
p1_lr = (m1_l, m1_l_l, m1_l_l_l, m1_l_l_l_l, m1_l05, m1_l1, m1_l15, m1_l2, m1_l25, m1_l3, m1_l35, m1_l4 , m1_l_05, m1_l_1, m1_l_15, m1_l_2, m1_l_25, m1_l_3, m1_l_35, m1_l_4)


m1_l05_l05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 0.5)  > (gf_copy.iloc[ind[i] - 2, 2] + 0.5)"
m1_l1_l1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1)  > (gf_copy.iloc[ind[i] - 2, 2] + 1)"
m1_l2_l2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 2)  > (gf_copy.iloc[ind[i] - 2, 2] + 2)"
m1_l05_l_05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 0.5)  > (gf_copy.iloc[ind[i] - 2, 2] - 0.5)"
m1_l1_l_1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1)  > (gf_copy.iloc[ind[i] - 2, 2] - 1)"
m1_l2_l_2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 2)  > (gf_copy.iloc[ind[i] - 2, 2] - 2)"
m1_l15_l15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] + 1.5)"
m1_l15_l2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] + 2)"
m1_l15_l1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] + 1)"
m1_l15_l05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] + 0.5)"
m1_l15_l_15 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] - 1.5)"
m1_l15_l_05 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] - 0.5)"
m1_l15_l_1 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] - 1)"
m1_l15_l_2 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i] - 1, 2] > (gf_copy.iloc[ind[i] - 2, 2] - 2)"
p2_lr = (m1_l05_l05, m1_l1_l1, m1_l2_l2, m1_l05_l_05, m1_l1_l_1 , m1_l2_l_2, m1_l15_l15, m1_l15_l2, m1_l15_l1, m1_l15_l05, m1_l15_l_15, m1_l15_l_05, m1_l15_l_1, m1_l15_l_2)


m1_l15_a_m1m0 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 0"
m1_l15_a_m1m05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 0.5"
m1_l15_a_m1m1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 1"
m1_l15_a_m1m15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 1.5"
m1_l15_a_m1m2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 2"
m1_l15_a_m1m25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] > 2.5"
m1_l15_a_m1l0 = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 0"
m1_l15_a_m1l05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 0.5"
m1_l15_a_m1l1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 1"
m1_l15_a_m1l15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 1.5"
m1_l15_a_m1l2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 2"
m1_l15_a_m1l25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and  gf_copy.iloc[ind[i], 2] < 2.5"
p3_lr = (m1_l15_a_m1m0, m1_l15_a_m1m05, m1_l15_a_m1m1, m1_l15_a_m1m15, m1_l15_a_m1m2, m1_l15_a_m1m25, m1_l15_a_m1l0, m1_l15_a_m1l05, m1_l15_a_m1l1, m1_l15_a_m1l15, m1_l15_a_m1l2, m1_l15_a_m1l25)

m1_l1_a_m1m0 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 0"
m1_l1_a_m1m05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 0.5"
m1_l1_a_m1m1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 1"
m1_l1_a_m1m15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 1.5"
m1_l1_a_m1m2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 2"
m1_l1_a_m1m25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > 2.5"
m1_l1_a_m1l0 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 0"
m1_l1_a_m1l05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 0.5"
m1_l1_a_m1l1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 1"
m1_l1_a_m1l15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 1.5"
m1_l1_a_m1l2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 2"
m1_l1_a_m1l25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < 2.5"
p4_lr = (m1_l1_a_m1m0, m1_l1_a_m1m05, m1_l1_a_m1m1, m1_l1_a_m1m15, m1_l1_a_m1m2, m1_l1_a_m1m25, m1_l1_a_m1l0, m1_l1_a_m1l05, m1_l1_a_m1l1, m1_l1_a_m1l15, m1_l1_a_m1l2, m1_l1_a_m1l25)


m1_l_1_a_m1m0 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 0"
m1_l_1_a_m1m05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 0.5"
m1_l_1_a_m1m1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 1"
m1_l_1_a_m1m15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 1.5"
m1_l_1_a_m1m2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > 2"
m1_l_1_a_m1l0 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 0"
m1_l_1_a_m1l05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 0.5"
m1_l_1_a_m1l1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 1"
m1_l_1_a_m1l15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 1.5"
m1_l_1_a_m1l2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < 2"
p5_lr = (m1_l_1_a_m1m0, m1_l_1_a_m1m05, m1_l_1_a_m1m1, m1_l_1_a_m1m15, m1_l_1_a_m1m2, m1_l_1_a_m1l0, m1_l_1_a_m1l05, m1_l_1_a_m1l1, m1_l_1_a_m1l15, m1_l_1_a_m1l2)


mrAM_LmrB15_a_mrAM1_a_mrBM0 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 0"
mrAM_LmrB15_a_mrAM1_a_mrBM05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 0.5"
mrAM_LmrB15_a_mrAM1_a_mrBM1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 1"
mrAM_LmrB15_a_mrAM1_a_mrBM15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 1.5"
mrAM_LmrB15_a_mrAM1_a_mrBM2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 2"
mrAM_LmrB15_a_mrAM1_a_mrBM25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 2.5"
mrAM_LmrB15_a_mrAM1_a_mrBM3 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 3"
mrAM_LmrB15_a_mrAM1_a_mrBM35 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > 3.5"
mrAM_LmrB15_a_mrAM1_a_mrBL0 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 0"
mrAM_LmrB15_a_mrAM1_a_mrBL05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 0.5"
mrAM_LmrB15_a_mrAM1_a_mrBL1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 1"
mrAM_LmrB15_a_mrAM1_a_mrBL15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 1.5"
mrAM_LmrB15_a_mrAM1_a_mrBL2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 2"
mrAM_LmrB15_a_mrAM1_a_mrBL25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 2.5"
mrAM_LmrB15_a_mrAM1_a_mrBL3 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 3"
mrAM_LmrB15_a_mrAM1_a_mrBL35 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < 3.5"
p6_lr = (mrAM_LmrB15_a_mrAM1_a_mrBM0, mrAM_LmrB15_a_mrAM1_a_mrBM05, mrAM_LmrB15_a_mrAM1_a_mrBM1, mrAM_LmrB15_a_mrAM1_a_mrBM15, mrAM_LmrB15_a_mrAM1_a_mrBM2,
         mrAM_LmrB15_a_mrAM1_a_mrBM25, mrAM_LmrB15_a_mrAM1_a_mrBM3, mrAM_LmrB15_a_mrAM1_a_mrBM35, mrAM_LmrB15_a_mrAM1_a_mrBL0, mrAM_LmrB15_a_mrAM1_a_mrBL05, mrAM_LmrB15_a_mrAM1_a_mrBL1,
         mrAM_LmrB15_a_mrAM1_a_mrBL15, mrAM_LmrB15_a_mrAM1_a_mrBL2, mrAM_LmrB15_a_mrAM1_a_mrBL25, mrAM_LmrB15_a_mrAM1_a_mrBL3, mrAM_LmrB15_a_mrAM1_a_mrBL35)


m1_l1_a_m1m_05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > -0.5"
m1_l1_a_m1m_1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > -1"
m1_l1_a_m1m_15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > -1.5"
m1_l1_a_m1m_2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > -2"
m1_l1_a_m1m_25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] > -2.5"
m1_l1_a_m1l_05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < -0.5"
m1_l1_a_m1l_1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < -1"
m1_l1_a_m1l_15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < -1.5"
m1_l1_a_m1l_2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < -2"
m1_l1_a_m1l_25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1) and  gf_copy.iloc[ind[i], 2] < -2.5"
p7_lr = (m1_l1_a_m1m_05, m1_l1_a_m1m_1, m1_l1_a_m1m_15, m1_l1_a_m1m_2, m1_l1_a_m1m_25, m1_l1_a_m1l_05, m1_l1_a_m1l_1, m1_l1_a_m1l_15, m1_l1_a_m1l_2, m1_l1_a_m1l_25)



m1_l_1_a_m1m_05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > - 0.5"
m1_l_1_a_m1m_1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > - 1"
m1_l_1_a_m1m_15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > - 1.5"
m1_l_1_a_m1m_2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > - 2"
m1_l_1_a_m1m_25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] > - 2.5"
m1_l_1_a_m1l_05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < - 0.5"
m1_l_1_a_m1l_1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < - 1"
m1_l_1_a_m1l_15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < - 1.5"
m1_l_1_a_m1l_2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] <  - 2"
m1_l_1_a_m1l_25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1) and  gf_copy.iloc[ind[i], 2] < - 2.5"
p8_lr = (m1_l_1_a_m1m_05, m1_l_1_a_m1m_1, m1_l_1_a_m1m_15, m1_l_1_a_m1m_2, m1_l_1_a_m1m_25, m1_l_1_a_m1l_05, m1_l_1_a_m1l_1, m1_l_1_a_m1l_15, m1_l_1_a_m1l_2, m1_l_1_a_m1l_25 )



mrAM_LmrB15_a_mrAM1_a_mrBM_05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -0.5"
mrAM_LmrB15_a_mrAM1_a_mrBM_1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -1"
mrAM_LmrB15_a_mrAM1_a_mrBM_15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -1.5"
mrAM_LmrB15_a_mrAM1_a_mrBM_2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -2"
mrAM_LmrB15_a_mrAM1_a_mrBM_25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -2.5"
mrAM_LmrB15_a_mrAM1_a_mrBM_3 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -3"
mrAM_LmrB15_a_mrAM1_a_mrBM_35 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] > -3.5"
mrAM_LmrB15_a_mrAM1_a_mrBL_05 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -0.5"
mrAM_LmrB15_a_mrAM1_a_mrBL_1 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -1"
mrAM_LmrB15_a_mrAM1_a_mrBL_15 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -1.5"
mrAM_LmrB15_a_mrAM1_a_mrBL_2 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -2"
mrAM_LmrB15_a_mrAM1_a_mrBL_25 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -2.5"
mrAM_LmrB15_a_mrAM1_a_mrBL_3 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -3"
mrAM_LmrB15_a_mrAM1_a_mrBL_35 = "gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] + 1.5) and gf_copy.iloc[ind[i], 2] > 1 and gf_copy.iloc[ind[i] - 1, 2] < -3.5"
p9_lr = (mrAM_LmrB15_a_mrAM1_a_mrBM_05, mrAM_LmrB15_a_mrAM1_a_mrBM_1, mrAM_LmrB15_a_mrAM1_a_mrBM_15, mrAM_LmrB15_a_mrAM1_a_mrBM_2, mrAM_LmrB15_a_mrAM1_a_mrBM_25, mrAM_LmrB15_a_mrAM1_a_mrBM_3,
          mrAM_LmrB15_a_mrAM1_a_mrBM_35, mrAM_LmrB15_a_mrAM1_a_mrBL_05, mrAM_LmrB15_a_mrAM1_a_mrBL_1, mrAM_LmrB15_a_mrAM1_a_mrBL_15, mrAM_LmrB15_a_mrAM1_a_mrBL_2, mrAM_LmrB15_a_mrAM1_a_mrBL_25,
          mrAM_LmrB15_a_mrAM1_a_mrBL_3, mrAM_LmrB15_a_mrAM1_a_mrBL_35)


p1_cr_plus1 = (m1_l_25, m1_l_2, m1_l, m1_m_m_m, m1_m1_a_m1l_05)


p1_plus1 =(m1_m_25, m1_m2)

p2_plus1 = (m1_m2_m2, m1_m25)

p3_plus1 = (m1_m15, m1_m1)

p4_plus1 = (m1_m4, m1_m3)

p5_plus1 = (m1_m35, m1_m_15)

p6_plus1 = (m1_l_25, mrAM_LmrB15_a_mrAM1_a_mrBL2)

p7_plus1 = (mrAM_MmrB15_a_mrAM1_a_mrBM3, mrAM_MmrB15_a_mrAM1_a_mrBM35)

p8_plus1 = (mrAM_MmrB15_a_mrAM1_a_mrBM25, mrAM_MmrB15_a_mrAM1_a_mrBM2)



if __name__ == '__main__':
    print(m1_m)
#酸碱平衡紊乱判断

x = float(input("pH="))
y = float(input("PaCO2(mmHg)="))
z = float(input("HCO3-(mmol/L)="))
if y > 45 and z < 24:
    print("呼酸并代酸")
elif y < 35 and z > 24:
    print("呼碱并代碱")
elif y > 45 and z > 24:
    if x > 7.4:  # HCO3-原发性增高
        a = 0.7 * (z - 24) + 5 + 40
        b = 0.7 * (z - 24) - 5 + 40  # 代谢性碱中毒的代偿公式
        if y <= a and y >= b:
            print("单纯代碱")
        else:
            print("呼酸合并代碱")
    elif x < 7.4:  # PaCO2原发性增高
        acute_or_chronic = input("急性or慢性=")
        acute = ("急性")
        chronic = ("慢性")
        if acute in acute_or_chronic:
            a = 0.1 * (y - 40) + 1.5 + 24
            b = 0.1 * (y - 40) - 1.5 + 24  # 急性呼酸中毒的代偿公式
            if z <= a and z >= b:
                print("单纯急性呼酸")
            else:
                print("呼酸合并代碱")
        elif chronic in acute_or_chronic:
            a = 0.35 * (y - 40) + 3 + 24
            b = 0.35 * (y - 40) - 3 + 24  # 慢性呼酸中毒的代偿公式
            if z <= a and z >= b:
                print("单纯慢性呼酸")
            else:
                print("呼酸合并代碱")
elif y < 45 and z < 24:
    if x < 7.4:  # HCO3-原发性减少
        a = 1.2 * (24 - z) + 2
        b = 1.2 * (24 - z) - 2  # 代谢性酸中毒的代偿公式
        if 40 - y <= a and 40 - y >= b:
            print("单纯代酸")
        else:
            print("呼碱合并代酸")
    elif x > 7.4:  # PaCO2原发性减少
        acute_or_chronic = input("急性or慢性=")
        acute = ("急性")
        chronic = ("慢性")
        if acute in acute_or_chronic:
            a = 0.2 * (40 - y) + 2.5
            b = 0.2 * (40 - y) - 2.5  # 急性呼碱中毒的代偿公式
            if 24 - z <= a and 24 - z >= b:
                print("单纯急性呼碱")
            else:
                print("呼碱合并代酸")
        elif chronic in acute_or_chronic:
            a = 0.5 * (40 - y) + 2.5
            b = 0.5 * (40 - y) - 2.5  # 慢性呼碱中毒的代偿公式
            if 24 - z <= a and 24 - z >= b:
                print("单纯慢性呼碱")
            else:
                print("呼碱合并代酸")

import math

# AT03

instance1  = ["high"    , "bad"    , "high", "none"    , "$0-$15k" ]
instance2  = ["high"    , "unknown", "high", "none"    , "$15-$35k"]
instance3  = ["moderate", "unknown", "low" , "none"    , "$15-$35k"]
instance4  = ["high"    , "unknown", "low" , "none"    , "$0-$15k" ]
instance5  = ["low"     , "unknown", "low" , "none"    , ">$35k"   ]
instance6  = ["low"     , "unknown", "low" , "adequate", ">$35k"   ]
instance7  = ["high"    , "bad"    , "low" , "none"    , "$0-$15k" ]
instance8  = ["moderate", "bad"    , "low" , "adequate", ">$35k"   ]
instance9  = ["low"     , "good"   , "low" , "none"    , ">$35k"   ]
instance10 = ["low"     , "good"   , "high", "adequate", ">$35k"   ]
instance11 = ["high"    , "good"   , "high", "none"    , "$0-$15k" ]
instance12 = ["moderate", "good"   , "high", "none"    , "$15-$35k"]
instance13 = ["low"     , "good"   , "high", "none"    , ">$35k"   ]
instance14 = ["high"    , "bad"    , "high", "none"    , "$15-$35k"]
data = [instance1, instance2, instance3, instance4, instance5, instance6, instance7, instance8, instance9, instance10, instance11, instance12, instance13, instance14]

# AP02

instance1 = [1 , "a", "a", "a"]
instance2 = [1 , "c", "b", "c"]
instance3 = [1 , "c", "a", "c"]
instance4 = [-1, "b", "a", "a"]
instance5 = [-1, "a", "b", "c"]
instance6 = [-1, "b", "b", "c"]
data = [instance1, instance2, instance3, instance4, instance5, instance6]

#AP01

instance1 = ["A", "A", "A"]
instance2 = ["A", "A", "A"]
instance3 = ["C", "A", "B"]
instance4 = ["C", "B", "B"]
instance5 = ["B", "B", "B"]
instance6 = ["B", "B", "B"]
data = [instance1, instance2, instance3, instance4, instance5, instance6]

# HW01

data  = []
# data += [["C", 0.22, 2, 0, 1]]
# data += [["B", 0.06, 0, 0, 0]]
# data += [["C", 0.16, 1, 2, 2]]
# data += [["B", 0.21, 0, 0, 0]]
# data += [["C", 0.01, 2, 2, 0]]
data += [["B", 0.3 , 0, 1, 0]]
data += [["A", 0.76, 0, 1, 1]]
# data += [["A", 0.86, 1, 0, 0]]
data += [["C", 0.93, 0, 1, 1]]
data += [["C", 0.47, 0, 1, 1]]
# data += [["A", 0.73, 1, 0, 0]]
# data += [["B", 0.89, 1, 2, 0]]

def entropy(data, i):
    
    hist = []
    for instance in data:
        found = False
        for pair in hist:
            value = pair[0]
            count = pair[1]
            if instance[i] == value:
                pair[1] += 1
                found = True
        if not found:
            hist += [[instance[i], 1]]

    total = len(data)

    entr = 0
    for pair in hist:
        entr -= pair[1]/total * math.log(pair[1]/total, 2)

    return entr

def entropy_cond(data, i, cond):

    hist = []
    for j in range(len(data)):
        found = False
        for pair in hist:
            value = pair[0]
            count = pair[1]
            if data[j][cond] == value:
                pair[1] += [j]
                found = True
        if not found:
            hist += [[data[j][cond], [j]]]
    
    total = len(data)

    entr = 0
    for pair in hist:
        data_subset = []
        for j in pair[1]:
            data_subset += [data[j]]
        entr += len(pair[1])/total * entropy(data_subset, i)

    return entr

def information_gain(data, i):
    return entropy(data, 0) - entropy_cond(data, 0, i)

def information_gain_cont(data, i):
    
    max_ig = 0
    cut = 0
    data = sorted(data, key=lambda x: x[i])
    for j in range(1, len(data)):
        if data[j - 1][i] != data[j][i]:
            data_subset1 = data[:j]
            data_subset2 = data[j:]
            entr = j / len(data) * entropy(data_subset1, 0) + (len(data) - j) / len(data) * entropy(data_subset2, 0)
            ig = entropy(data, 0) - entr
            if ig > max_ig:
                max_ig = ig
                cut = (data[j][i] + data[j - 1][i]) / 2

    return max_ig, cut

print(f"IG(y{1}) = {round(information_gain_cont(data, 1)[0], 3), information_gain_cont(data, 1)[1]}")
for i in range(2, 5):
    print(f"IG(y{i}) = {round(information_gain(data, i), 3)}")
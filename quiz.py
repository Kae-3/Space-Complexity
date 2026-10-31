def direct_access(scores_dict, student_id):
    return scores_dict.get(student_id, "Not Found")

def linear_search(scores_list, target_score):
    for i, score in enumerate(scores_list):
        if score == target_score:
            return i
    return -1

def pair_comparison(scores_list):
    pairs = []
    for i in range(len(scores_list)):
        for j in range(i + 1, len(scores_list)):
            pairs.append((scores_list[i], scores_list[j]))
    return pairs

scores_dict = {101: 85, 102: 92, 103: 78}
scores_list = [85, 92, 78, 90]
print(direct_access(scores_dict, 102))
print(linear_search(scores_list, 78))
print(pair_comparison(scores_list))
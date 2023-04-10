from collections import defaultdict,Counter
import matplotlib.pyplot as plt

def vectorsum(v1,v2):
    assert len(v1) == len(v2)
    return [n1+n2 for n1,n2 in zip(v1,v2)]

def mean(v):
    return sum(v)/len(v)

def median(v):
    if len(v)%2 != 0:
        return v[len(v)//2]
    return (v[len(v)//2] + v[len(v)//2 - 1])/2

def mode(v):
    weight_freq = Counter(v)
    max_weight_freq = max(weight_freq.values())
    return [weight for weight in weight_freq if weight_freq[weight] == max_weight_freq]
    
def variance(data,mean):
    return sum([(value-mean)**2 for value in data])/(len(data)-1)
    
def covariance(data_,data__,mean_,mean__):
    return sum([(d_ - mean_) * (d__ - mean__) for d_,d__ in zip(data_,data__)])/(len(data_)-1)

def q1(data):
    age_group = defaultdict(list)
    for user in data:
        if user['Age'] <= 20:
            age_group['less or equal to 20'].append(user['user_id'])
        elif user['Age'] > 20 and user['Age'] <= 40:
            age_group['between 20 and 40'].append(user['user_id'])
        else:
            age_group['more than 40'].append(user['user_id'])
    print('age groups of users : ')
    for group in age_group:
        print(group,' : ',age_group[group])

def q2(data):
    user_ids = [user['user_id'] for user in data]    
    weights = [user['Weight'] for user in data]
    plt.plot(user_ids,weights,marker='o',markeredgecolor='black',linestyle='dashed',label='Question2')
    plt.xlabel('user_id')
    plt.ylabel('weights')
    plt.title('user_id vs weights')
    plt.legend()
    plt.savefig('idsupma1q2.png',dpi=1200)
    plt.show()

def q3(data):
    users_data = [[user['Height'],user['Weight'],user['Age']] for user in data]
    users_data_sum = [0 for index in range(len(users_data[0]))]
    for user in users_data:
        users_data_sum = vectorsum(users_data_sum,user)
    print('sum of users height, weight and age : ',users_data_sum)
    avg_height = users_data_sum[0]/len(users_data);
    avg_weight = users_data_sum[1]/len(users_data);
    avg_age = users_data_sum[2]/len(users_data);
    print('average height : ',avg_height)
    print('average weight : ',avg_weight)
    print('average age : ',avg_age)
 
def q4(data):
    weights = [user['Weight'] for user in data]
    mean_weight = mean(weights)
    print('mean_weight : ',mean_weight)
    median_weight = median(weights)
    print('median_weight : ',median_weight)
    mode_weight = mode(weights)
    print('mode_weight : ',mode_weight)

def q5(data):
    heights = [user['Height'] for user in data]
    mean_height = mean(heights)
    data_variance =  variance(heights,mean_height)
    print('Variance of heights of users : ',data_variance)
    
def q6(data):
    heights = [user['Height'] for user in data]
    weights = [user['Weight'] for user in data]
    mean_height = mean(heights)
    mean_weight = mean(weights)
    data_covariance = covariance(heights,weights,mean_height,mean_weight)
    print('Covariance between heights and weights of users : ',data_covariance)
 
def main():
    data = [    {"user_id" : 1, "Height" : 150, "Weight" : 60, "Age" : 23},
                 {"user_id" : 2, "Height" : 130, "Weight" : 40, "Age" : 15},
                 {"user_id" : 3, "Height" : 155, "Weight" : 62, "Age" : 25},
                 {"user_id" : 4, "Height" : 120, "Weight" : 42, "Age" : 12},
                 {"user_id" : 5, "Height" : 180, "Weight" : 90, "Age" : 45},
                 {"user_id" : 6, "Height" : 184, "Weight" : 90, "Age" : 50},
                 {"user_id" : 7, "Height" : 190, "Weight" : 95, "Age" : 55},
                 {"user_id" : 8, "Height" : 189, "Weight" : 93, "Age" : 53},
                 {"user_id" : 9, "Height" : 188, "Weight" : 92, "Age" : 58},
                 {"user_id" : 10, "Height" : 190, "Weight" : 95, "Age" : 55},
                 {"user_id" : 11, "Height" : 170, "Weight" : 65, "Age" : 39},
                 {"user_id" : 12, "Height" : 165, "Weight" : 60, "Age" : 35},
                 {"user_id" : 13, "Height" : 160, "Weight" : 55, "Age" : 30},
                 {"user_id" : 14, "Height" : 155, "Weight" : 57, "Age" : 25},
                 {"user_id" : 15, "Height" : 149, "Weight" : 54, "Age" : 22},
                 {"user_id" : 16, "Height" : 100, "Weight" : 30, "Age" : 11},
                 {"user_id" : 17, "Height" : 110, "Weight" : 40, "Age" : 16},
                 {"user_id" : 18, "Height" : 119, "Weight" : 45, "Age" : 19},
                 {"user_id" : 19, "Height" : 120, "Weight" : 50, "Age" : 39},
                 {"user_id" : 20, "Height" : 170, "Weight" : 80, "Age" : 75}
             ]   
    
    print('Question 1  ')
    print('------------')
    q1(data)
    q2(data)
    print('\nQuestion 3  ')
    print('------------')
    q3(data)
    print('\nQuestion 4  ')
    print('------------')
    q4(data)
    print('\nQuestion 5  ')
    print('------------')
    q5(data)
    print('\nQuestion 6  ')
    print('------------')
    q6(data)
    
if __name__ == '__main__':
    main()

import numpy as np

def calculate(a):
    
    if len(a) < 9 or len(a) > 9:
        
        raise ValueError('List must contains nine numbers')
    
    else:
    
        # Reshaping
        
        new_arr = np.reshape(a, (3, 3))
        
        # Mean, Variance, Standard deviation, Max, Min and Sum
        
        mean_1 = np.mean(new_arr, axis = 0).tolist()
        mean_2 = np.mean(new_arr, axis = 1).tolist()
        mean = np.mean(new_arr)
        
        var_1 = np.var(new_arr, axis = 0).tolist()
        var_2 = np.var(new_arr, axis = 1).tolist
        variance = np.var(new_arr)
        
        standard_deviation_1 = np.std(new_arr, axis = 0).tolist()
        standard_deviation_2 = np.std(new_arr, axis = 1).tolist()
        standard_deviation = np.std(new_arr)
        
        max_1 = np.max(new_arr, axis = 0).tolist()
        max_2 = np.max(new_arr, axis = 1).tolist()
        maximum = np.max(new_arr)
        
        min_1 = np.min(new_arr, axis = 0).tolist()
        min_2 = np.min(new_arr, axis = 1).tolist()
        minimum = np.min(new_arr).tolist()
        
        sum1 = np.sum(new_arr, axis = 0).tolist()
        sum2 = np.sum(new_arr, axis = 1).tolist()
        sum_of_elements = np.sum(new_arr)
        
        # Returning data    

        return {
            'mean' : [mean_1, mean_2, mean],
            'variance' : [var_1, var_2, variance],
            'standard deviation' : [standard_deviation_1, standard_deviation_2, standard_deviation],
            'max' : [max_1, max_2, maximum],
            'min' : [min_1, min_2, minimum],
            'sum' : [sum1, sum2, sum_of_elements]
            }
        


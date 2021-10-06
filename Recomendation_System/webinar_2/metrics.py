import numpy as np

def precision(recommended_list, bought_list):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    flags = np.isin(bought_list, recommended_list)
    
    precision = flags.sum() / len(recommended_list)
    
    return precision


def precision_at_k(recommended_list, bought_list, k=5):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    bought_list = bought_list  # Тут нет [:k] !!
    recommended_list = recommended_list[:k]
    
    flags = np.isin(bought_list, recommended_list)
    
    precision = flags.sum() / len(recommended_list)
    
    
    return precision


def money_precision_at_k(recommended_list, bought_list, prices_recommended, k=5):
        
    # your_code
    # Лучше считать через матричное произведение, а не цикл
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)
    
    recommended_list = recommended_list[:k]
    prices_recommended = prices_recommended[:k]
    
    # Почему здесь изменен порядок в функции isin?
    flags = np.isin(recommended_list, bought_list)
    
    relevant_revenue = (flags * prices_recommended).sum()
    recommended_revenue = prices_recommended.sum()
    
    precision = relevant_revenue / recommended_revenue
    
    return precision

def recall(recommended_list, bought_list):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    flags = np.isin(bought_list, recommended_list)
    
    recall = flags.sum() / len(bought_list)
    
    return recall


def recall_at_k(recommended_list, bought_list, k=5):
    
    # your code
    recall_at_k = recall(recommended_list[:k], bought_list)
    
    return recall_at_k


def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k=5):
    
    # your_code
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)
    prices_bought = np.array(prices_bought)

    
    assert recommended_list.shape == prices_recommended.shape
    assert bought_list.shape == prices_bought.shape
    
    
    recommended_list = recommended_list[:k]
    prices_recommended = prices_recommended[:k]
    
    
    flags = np.isin(bought_list, recommended_list)
    
    money_recall = (flags * prices_bought).sum() / (prices_bought).sum()
    
    return money_recall
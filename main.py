#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:55:52 2023

@author: A00315995

# Program Name: main.py
# purpose: This program reads a dataset containing 500 of the most profitable hollywood movies from 1970's till the 2020's and performs statistical and visual analysis on it.
"""
from math import sqrt
import matplotlib.pyplot as plt
import sys

DATASET = "dataset.csv"


def display_menu():
    """
    The function loads data including budget, worldwide gross, title, decade frequency
    dictionary, and decade numerical dictionary. It presents a menu to perform various
    analyses and visualizations based on user selections.

    Returns
    -------
    None.

    """
    print("#" * 50 + " Program Info " + "#" * 50)
    print(
        "\nThis program reads a dataset containing 500 of the most profitable hollywood movies from 1970's till the 2020's. \nIt further provides statistical and visual analysis on the dataset.\n")
    print("#" * 114)
    budget, worldwide_gross, title, decade_freq_dict, decade_numerical_dict = load_dataset()
    while True:
        print("\n----------/// MENU ///----------\n")
        main_menu_choice1 = input(
            "1. Display statistical analysis\n2. Display visualisations\n3. Exit program\n\nPlease select your choice: ")
        if main_menu_choice1 == '1':
            statistical(budget, worldwide_gross, title, decade_freq_dict, decade_numerical_dict)
        elif main_menu_choice1 == '2':
            visualisation(budget, worldwide_gross, decade_freq_dict, decade_numerical_dict)
        elif main_menu_choice1 == '3':
            print("\nProgram is exiting... Good Bye!")
            sys.exit()
        else:
            print("\nInvalid Choice, Please try again...\n\n")


def statistical(budget, worldwide_gross, title, decade_freq_dict, decade_numerical_dict):
    """
    This function provides statistical analysis based on numerical columns (Budgets, Worldwide Gross)
    and categorical data (Decade). It prompts the user to select various analysis options and displays
    computations accordingly.

    Parameters
    ----------
    budget : list
        A list of movie budgets.
    worldwide_gross : list
        A list of worldwide gross earnings for movies.
    title : list
        A list of movie titles.
    decade_freq_dict : dict
        A dictionary with decades as keys and frequency of movies per decade.
    decade_numerical_dict : dict
        A dictionary with decades as keys and associated worldwide gross data.

    Returns
    -------
    None.

    """
    while True:
        choice = input("\nAnalysis based on numerical columns (Budgets, Worldwide Gross)\n"
                       "--------------------------------------------------------------\n"
                       "1. Number of values in Budgets and Worldwide Gross\n"
                       "2. Mean of the Budgets and Worldwide Gross\n"
                       "3. Median of the Budgets and Worldwide Gross\n"
                       "4. Mode of the Budgets and Worldwide Gross\n"
                       "5. Maximum of the Budgets and Worldwide Gross\n"
                       "6. Minimum of the Budgets and Worldwide Gross\n"
                       "7. Range of the Budgets and Worldwide Gross\n"
                       "8. Inter-Quartile Range of the Budgets and Worldwide Gross\n"
                       "9. Standard Deviation of the Budgets and Worldwide Gross\n"
                       "10. Skewness of the Budgets and Worldwide Gross\n"
                       "11. Correlation between Budgets and Worldwide Gross\n"
                       "\nAnalysis based on category (Decade)\n"
                       "-----------------------------------\n"
                       "12. Number of distinct sub-categories\n"
                       "13. Decade with the highest number of profitable movies\n"
                       "14. Decade with the lowest number of profitable movies\n"
                       "15. Decade with the highest total gross\n"
                       "16. Decade with the lowest total gross\n"
                       "\nPlease select your choice (1-16), Press Q or q to go back to main menu: \n\n")
        print("\n\n")
        if choice == '1':
            print(f"Number of values in budget: {len(budget)}")
            print(f"Number of values in Worldwide Gross: {len(worldwide_gross)}")
        elif choice == '2':
            print(f"Mean of the budgets of the most profitable movies: {calculate_mean(budget):.2f} million USD")
            print(
                f"Mean of the worldwide grosses of the most profitable movies: {calculate_mean(worldwide_gross):.2f} million USD")
        elif choice == '3':
            print(f"Median of the budgets of the most profitable movies: {calculate_median(budget):.2f} million USD")
            print(
                f"Median of the worldwide grosses of the most profitable movies: {calculate_median(worldwide_gross):.2f} million USD")
        elif choice == '4':
            print(f"Mode of the budgets of the most profitable movies: {calculate_mode(budget):.2f} million USD")
            print(
                f"Mode of the worldwide grosses of the most profitable movies: {calculate_mode(worldwide_gross):.2f} million USD")
        elif choice == '5':
            print(
                f"Maximum budget of the most profitable movie: {max(budget):.2f} million USD ({title[budget.index(max(budget))]})")
            print(
                f"Maximum worldwide gross of the most profitable movie: {max(worldwide_gross):.2f} million USD ({title[worldwide_gross.index(max(worldwide_gross))]})")
        elif choice == '6':
            print(
                f"Minimum budget of the most profitable movie: {min(budget):.2f} million USD ({title[budget.index(min(budget))]})")
            print(
                f"Minimum worldwide gross of the most profitable movie: {min(worldwide_gross):.2f} million USD ({title[worldwide_gross.index(min(worldwide_gross))]})")
        elif choice == '7':
            print(f"Range of the budgets of the most profitable movies: {calculate_range(budget)} million USD")
            print(
                f"Range of the worldwide grosses of the most profitable movies: {calculate_range(worldwide_gross)} million USD")
        elif choice == '8':
            print(
                f"Inter-quartile range of budgets of the most profitable movies: {calculate_interquartile(budget):.2f} million USD")
            print(
                f"Inter-quartile range of worldwide grosses of the most profitable movies: {calculate_interquartile(worldwide_gross)} million USD")
        elif choice == '9':
            print(
                f"Standard Deviation of the budgets of the most profitable movies: {calculate_std_deviation(budget)} million USD")
            print(
                f"Standard Deviation of the worldwide grosses of the most profitable movies: {calculate_std_deviation(worldwide_gross)} million USD")
        elif choice == '10':
            print(
                f"Pearson Mode Skewness of the budgets of the most profitable movies: {calculate_skewness(budget, True)}")
            print(
                f"Alternative Pearson Mode Skewness of the budgets of the most profitable movies: {calculate_skewness(budget, False)}")
            print(
                f"Pearson Mode Skewness of the worldwide grosses of the most profitable movies: {calculate_skewness(worldwide_gross, True)}")
            print(
                f"Alternative Pearson Mode Skewness of the worldwide grosses of the most profitable movies: {calculate_skewness(worldwide_gross, False)}")
        elif choice == '11':
            print(f"Correlation value of budget with worldwide gross: {calculate_correlation(budget, worldwide_gross)}")
        elif choice == '12':
            print(
                f"Number of distinct sub-categories: {len(decade_freq_dict)} ({', '.join(str(key) for key in decade_freq_dict.keys())})")
        elif choice == '13':
            print(
                f"The decade with the highest number of profitable movies is the {max(decade_freq_dict, key=decade_freq_dict.get)} with {max(decade_freq_dict.values())} movies")
        elif choice == '14':
            print(
                f"The decade with the lowest number of profitable movies is the {min(decade_freq_dict, key=decade_freq_dict.get)} with {min(decade_freq_dict.values())} movies")
        elif choice == '15':
            category_highest_gross(decade_numerical_dict)
        elif choice == '16':
            category_lowest_gross(decade_numerical_dict)
        elif choice.lower() == 'q':
            break
        else:
            print("\nInvalid Choice!")
        input("\nPress any key to display sub-menu again...\n\n")


def visualisation(budget, worldwide_gross, decade_freq_dict, decade_numerical_dict):
    """
    The function continuously displays a menu to the user, prompting them to select from different
    visualization options for both numerical (Budgets, Worldwide Gross) and categorical data (Decade).

    Parameters
    ----------
    budget : list
        A list of movie budgets.
    worldwide_gross : list
        A list of worldwide gross earnings for movies.
    decade_freq_dict : dict
        A dictionary with decades as keys and frequency of movies per decade.
    decade_numerical_dict : dict
        A dictionary with decades as keys and associated worldwide gross data.

    Returns
    -------
    None.

    """
    while True:
        choice = input("\nVisualisations based on numerical columns (Budgets, Worldwide Gross)\n"
                       "--------------------------------------------------------------------\n"
                       "1. Histogram of Budgets\n"
                       "2. Histogram of Worldwide Gross\n"
                       "3. Box plot of Budgets\n"
                       "4. Box plot of Worldwide Gross\n"
                       "5. Scatter plot of Budget vs Worldwide Gross\n"
                       "\nVisualisations based on category (Decade)\n"
                       "-----------------------------------------\n"
                       "6. Pie chart showing the percentage number of profitable movies in each decade\n"
                       "7. Bar chart showing the total of the profitable movies in each decade\n"
                       "8. Box plots of the worldwide grosses for each decade\n"
                       "\nPlease select your choice (1-8), Press Q or q to go back to main menu: \n\n")
        if choice == '1':
            show_budget_histogram(budget)
        elif choice == '2':
            show_gross_histogram(worldwide_gross)
        elif choice == '3':
            show_budget_boxplot(budget)
        elif choice == '4':
            show_gross_boxplot(worldwide_gross)
        elif choice == '5':
            show_scatterplot(budget, worldwide_gross)
        elif choice == '6':
            show_piechart(decade_freq_dict)
        elif choice == '7':
            show_barchart(decade_freq_dict)
        elif choice == '8':
            show_category_boxplot(decade_numerical_dict)
        elif choice.lower() == 'q':
            break
        else:
            print("\nInvalid Choice!")
        input("\nPress any key to display sub-menu again...\n\n")


def load_dataset():
    """
    This function reads the dataset file 'dataset.csv', extracts movie information,
    including budget, worldwide gross, and title. It organizes this information into lists
    and dictionaries categorized by decade, storing frequencies and worldwide gross for each decade.

    Returns
    -------
    budget : list
        A list of movie budgets.
    worldwide_gross : list
        A list of worldwide gross earnings for movies.
    title : list
        A list of movie titles.
    decade_freq_dict : dict
        A dictionary with decades as keys and frequency of movies per decade.
    decade_numerical_dict : dict
        A dictionary with decades as keys and associated worldwide gross data.

    """
    budget = list()
    worldwide_gross = list()
    title = list()
    decade_freq_dict = dict()
    decade_numerical_dict = dict()
    try:
        with open(DATASET) as datafile:
            _ = datafile.readline()
            for line in datafile:
                temp_list = line.strip().split(",")
                try:
                    temp_budget_holder = float(temp_list[2])
                    temp_gross_holder = float(temp_list[3])
                    budget.append(temp_budget_holder)
                    worldwide_gross.append(temp_gross_holder)
                    title.append(temp_list[1])
                    if temp_list[0] not in decade_numerical_dict:
                        decade_numerical_dict[temp_list[0]] = [float(temp_list[3])]
                    else:
                        decade_numerical_dict[temp_list[0]].append(float(temp_list[3]))
                    if temp_list[0] not in decade_freq_dict:
                        decade_freq_dict[temp_list[0]] = 1
                    else:
                        decade_freq_dict[temp_list[0]] += 1
                except ValueError:
                    print(f"\n\nUnable to convert value to float at line: {line}")

    except FileNotFoundError:
        print(
            "\n\nDataset file 'dataset.csv' not found in project location.\n\nPlease check if the file is present in the project folder or it hasn't been renamed.\n\nProgram is exiting...")
        sys.exit()
    return budget, worldwide_gross, title, decade_freq_dict, decade_numerical_dict


def calculate_mean(data_list):
    """
    This function computes the mean (average) for a given list of numerical data.

    Parameters
    ----------
    data_list : list
        A list containing numeric values.

    Returns
    -------
    float
        The mean (average) of the provided data.

    """
    return sum(data_list) / len(data_list)


def calculate_median(data_list):
    """
    This function computes the median (middle value) for a given list of numerical data.

    Parameters
    ----------
    data_list : list
        A list containing numeric values.

    Returns
    -------
    float
        The median of the provided data.

    """
    sorted_list = sorted(data_list)
    mid_index = int(len(sorted_list) / 2)
    if len(sorted_list) % 2:
        return sorted_list[mid_index]
    else:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2


def calculate_mode(data_list):
    """
    This function computes the mode (most frequently occurring value) for a given list of data.

    Parameters
    ----------
    data_list : list
        A list containing numeric or categorical values.

    Returns
    -------
    float
        The mode of the provided data.

    """
    frequencies = []
    for value in data_list:
        frequencies.append(data_list.count(value))
    return data_list[frequencies.index(max(frequencies))]


def calculate_range(data_list):
    """
    Calculate the range of a given list of numerical data.

    Parameters
    ----------
    data_list : list
        A list containing numerical values.

    Returns
    -------
    float
        The range of the data, rounded to two decimal places.

    """
    return round(max(data_list) - min(data_list), 2)


def calculate_interquartile(data_list):
    """
    This function computes the interquartile range (IQR) for a given list of numerical data.

    Parameters
    ----------
    data_list : list
        A list containing numeric values.

    Returns
    -------
    float
        The interquartile range (IQR) of the provided data.

    """
    sorted_list = sorted(data_list)
    mid_index = int(len(sorted_list) / 2)
    if len(sorted_list) % 2:
        lower_half = sorted_list[:mid_index]
        upper_half = sorted_list[mid_index + 1:]
    else:
        lower_half = sorted_list[:mid_index]
        upper_half = sorted_list[mid_index:]
    return calculate_median(upper_half) - calculate_median(lower_half)


def calculate_std_deviation(data_list):
    """
    This function computes the standard deviation for a given list of numerical data.

    Parameters
    ----------
    data_list : list
        A list containing numeric values..

    Returns
    -------
    float
        The standard deviation of the provided data.

    """
    mean = calculate_mean(data_list)
    sqrd_deviation = [(values - mean) ** 2 for values in data_list]
    return round(sqrt(sum(sqrd_deviation) / (len(data_list) - 1)), 2)


def calculate_skewness(data_list, flag):
    """
    This function computes the Pearson Mode Skewness or Alternative Pearson Mode Skewness measure for a given list of numerical data.

    Parameters
    ----------
    data_list : list
        A list containing numeric values.

    Returns
    -------
    float
        The skewness measure of the provided data.

    """
    try:
        if flag == True:
            return round((calculate_mean(data_list) - calculate_mode(data_list)) / calculate_std_deviation(data_list),
                         2)
        else:
            return round(
                3 * (calculate_mean(data_list) - calculate_median(data_list)) / calculate_std_deviation(data_list), 2)
    except ZeroDivisionError:
        print("\n\nDivision by zero encountered.\nRedirecting to main menu...\n\n")
        display_menu()


def calculate_correlation(budget_list, gross_list):
    """
    This function computes the correlation coefficient between two sets of numerical data, 'budget_list' and 'gross_list', using the Pearson correlation formula. 

    Parameters
    ----------
    budget_list : list
        A list containing numeric values representing movie budgets.
    gross_list : list
        A list containing numeric values representing worldwide gross earnings.

    Returns
    -------
    float
        The correlation coefficient between the provided lists.

    """
    try:
        budget_mean = calculate_mean(budget_list)
        gross_mean = calculate_mean(gross_list)
        budget_deviation = [value - budget_mean for value in budget_list]
        gross_deviation = [value - gross_mean for value in gross_list]
        budget_gross_deviations = [x * y for (x, y) in zip(budget_deviation, gross_deviation)]
        budget_sq_deviation = [(value - budget_mean) ** 2 for value in budget_list]
        gross_sq_deviation = [(value - gross_mean) ** 2 for value in gross_list]
        return round(sum(budget_gross_deviations) / (sqrt(sum(budget_sq_deviation)) * sqrt(sum(gross_sq_deviation))), 2)
    except ZeroDivisionError:
        print("\n\nDivision by zero encountered.\nRedirecting to main menu...\n\n")
        display_menu()


def show_budget_histogram(budget_list):
    """
    This function creates a histogram displaying the distribution of budgets for movies.
    The 'budget_list' parameter contains the data points for the histogram.
    The plot shows the frequency of movies within certain budget ranges.

    Parameters
    ----------
    budget_list : list
        A list containing budget values (in million USD) for movies.

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_title("Budgets of Most Profitable Movies")
    ax.set_xlabel("Budget (in million USD)")
    ax.set_ylabel("Number of movies")
    bins = range(0, int(max(budget_list)) + 50, 50)
    ax.set_xticks(bins)
    ax.hist(budget_list, bins, ec="black")
    plt.show()


def show_gross_histogram(gross_list):
    """
    This function creates a histogram displaying the distribution of worldwide gross for movies. 
    The 'gross_list' parameter contains the data points for the histogram.
    The plot shows the frequency of movies within certain gross ranges.

    Parameters
    ----------
    gross_list : list
        A list of worldwide gross values (in million USD).

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_title("Worldwide Gross of Most Profitable Movies")
    ax.set_xlabel("Worldwide gross (in million USD)")
    ax.set_ylabel("Number of movies")
    bins = range(0, int(max(gross_list)) + 200, 200)
    ax.set_xticks(bins)
    ax.hist(gross_list, bins, ec="black")
    plt.show()


def show_budget_boxplot(budget_list):
    """
    This function creates a box plot displaying the distribution of budgets for movies.
    The 'budget_list' parameter contains the data points for the box plot.
    The plot shows the median, quartiles, and excludes outliers of the budget values.

    Parameters
    ----------
    budget_list : list
        A list of budget values (in million USD).

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots()
    ax.set_title("Budgets of Most Profitable Movies")
    ax.set_ylabel("Budget (in million USD)")
    ax.boxplot(budget_list, showfliers=False, showmeans=True, meanline=True)
    plt.show()


def show_gross_boxplot(gross_list):
    """
    This function creates a box plot displaying the distribution of worldwide gross for movies. 
    The 'gross_list' parameter contains the data points for the box plot.
    The plot shows the median, quartiles, and excludes outliers of the gross values.

    Parameters
    ----------
    gross_list : list
        A list of worldwide gross values (in million USD).

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots()
    ax.set_title("Worldwide Gross of Most Profitable Movies")
    ax.set_ylabel("Worldwide gross (in million USD)")
    ax.boxplot(gross_list, showfliers=False, showmeans=True, meanline=True)
    plt.show()


def show_scatterplot(budget_list, gross_list):
    """
    This function creates a scatter plot displaying the relationship between budget and worldwide gross. 
    It plots the values from the 'budget_list' on the x-axis and the values from the 'gross_list' on the y-axis.

    Parameters
    ----------
    budget_list : list
        A list of budget values (in million USD).
    gross_list : list
        A list of worldwide gross values (in million USD).

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_title("Scatter Plot of Budget vs Worldwide gross")
    ax.set_xlabel("Budget (in million USD)")
    ax.set_ylabel("Worldwide gross (in million USD)")
    ax.scatter(budget_list, gross_list, marker='.')
    plt.show()


def category_highest_gross(decade_numerical_dict):
    """
    This function iterates through the input dictionary, computes the total gross earnings for each decade, and identifies the decade with the highest total gross earnings.
    It then prints the decade and its total gross in billion USD.

    Parameters
    ----------
    decade_numerical_dict : dict
        A dictionary where keys represent decades and values are lists of worldwide gross values.

    Returns
    -------
    None.

    """
    max_total = 0.0
    key_for_max_total = ""
    for key, value in decade_numerical_dict.items():
        temp = sum(value)
        if temp >= max_total:
            max_total = temp
            key_for_max_total = key
    print(f"The highest grossing decade is the {key_for_max_total} with a total of {max_total / 1000:.2f} Billion USD")


def category_lowest_gross(decade_numerical_dict):
    """
    This function iterates through the input dictionary, computes the total gross earnings for each decade, and identifies the decade with the lowest total gross earnings.
    It then prints the decade and its total gross in billion USD.

    Parameters
    ----------
    decade_numerical_dict : dict
        A dictionary where keys represent decades and values are lists of worldwide gross values.

    Returns
    -------
    None.

    """
    min_total = float("inf")  # Set initial smallest value to positive infinity
    key_for_min_total = ""
    for key, value in decade_numerical_dict.items():
        temp = sum(value)
        if temp <= min_total:
            min_total = temp
            key_for_min_total = key
    print(f"The lowest grossing decade is the {key_for_min_total} with a total of {min_total / 1000:.2f} Billion USD")


def show_piechart(decade_freq_dict):
    """
    This function takes a dictionary containing decades as keys and the frequency of movies as values.
    It generates a pie chart to visualize the percentage distribution of movies for each decade among the most profitable movies.

    Parameters
    ----------
    decade_freq_dict : dict
        A dictionary where keys represent decades and values denote the frequency of movies.

    Returns
    -------
    None.

    """
    decade_freq_dict = {k: decade_freq_dict[k] for k in sorted(decade_freq_dict)}
    fig, ax = plt.subplots(figsize=(10, 7))
    colors_list = ['tomato', 'cornflowerblue', 'gold', 'orchid', 'greenyellow', 'cyan']
    ax.set_title("Distribution of Most Profitable Movies by Decade")
    ax.pie(decade_freq_dict.values(), labels=decade_freq_dict.keys(), autopct="%.0f%%", pctdistance=0.8,
           colors=colors_list)
    plt.show()


def show_barchart(decade_freq_dict):
    """
    This function takes a dictionary containing decades as keys and the frequency of movies as values. 
    It generates a horizontal bar chart to visualize the frequency of profitable movies for each decade.

    Parameters
    ----------
    decade_freq_dict : dict
        A dictionary where keys represent decades and values denote the frequency of movies.

    Returns
    -------
    None.

    """
    decade_freq_dict = {k: decade_freq_dict[k] for k in sorted(decade_freq_dict)}
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_title("Most Profitable Movies in each Decade")
    ax.set_xlabel("Number of Movies")
    ax.set_ylabel("Decade")
    for index, value in enumerate(decade_freq_dict.values()):
        ax.text(value, index - 0.1, str(value))
    ax.barh(list(decade_freq_dict.keys()), decade_freq_dict.values())
    plt.show()


def show_category_boxplot(decade_numerical_dict):
    """
    This function takes a dictionary containing decades as keys and corresponding worldwide gross as values.
    It then generates a boxplot to visualize the distribution of worldwide gross for each decade without displaying outliers.

    Parameters
    ----------
    decade_numerical_dict : dict
        A dictionary where keys represent decades and values are worldwide gross list.

    Returns
    -------
    None.

    """
    decade_numerical_dict = {k: decade_numerical_dict[k] for k in sorted(decade_numerical_dict)}
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_title("Worldwide Gross for each Decade")
    ax.set_xlabel("Decade")
    ax.set_ylabel("Worldwide Gross (in million USD)")
    ax.boxplot(decade_numerical_dict.values(), showfliers=False, labels=decade_numerical_dict.keys(), showmeans=True,
               meanline=True)
    plt.show()


if __name__ == '__main__':
    display_menu()

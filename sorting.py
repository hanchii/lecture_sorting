import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode = "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
        return data


def selection_sort(numbers_array, direction="ascending"):
    for i in range(len(numbers_array)):
        min_idx = i
        for num_idx in range(i + 1, len(numbers_array)):
            if direction == "ascending":
                if numbers_array[min_idx] > numbers_array[num_idx]:
                    min_idx = num_idx
            elif direction == "descending":
                if numbers_array[min_idx] < numbers_array[num_idx]:
                    min_idx = num_idx
        numbers_array[i], numbers_array[min_idx] = numbers_array[min_idx], numbers_array[i]
    return numbers_array




def main():
    data = read_data("numbers.csv")
    sorted_array = selection_sort(data["series_1"].copy(), direction="descending")
    print(data["series_1"])
    print(sorted_array)


if __name__ == '__main__':
    main()

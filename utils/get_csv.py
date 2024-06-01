import os
import csv

from .llm_pipeline import llm_pipeline

def get_csv (file_path):
    answer_generation_chain, ques_list = llm_pipeline(file_path)
    base_folder = 'static/output/'

    if not os.path.isdir(base_folder):
        os.mkdir(base_folder)

    output_file = base_folder+"QA.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Вопрос", "Ответ"])

        for question in ques_list:
            print("Вопрос: ", question)
            answer = answer_generation_chain.run(question)
            print("Ответ: ", answer)
            print("--------------------------------------------------\n\n")

            csv_writer.writerow([question, answer])
    return output_file

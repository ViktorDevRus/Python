import os
import win32com.client

files_rtf = []
folder = r"C:\Users\PythonUser\PythonProjects\pythonProject1\tests\converted-to-docx"
for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith('rtf') and not file.startswith('~'):
            files_rtf.append(os.path.join(root, file))
for all_rtf in files_rtf:    
    word = win32com.client.Dispatch('Word.Application')
    wb = word.Documents.Open(all_rtf)
    wb.SaveAs2(all_rtf.replace('rtf', 'docx'), FileFormat=16)
    wb.Close()

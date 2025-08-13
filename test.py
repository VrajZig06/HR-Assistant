
import csv
Employee = []
with open("EmployeData/employeeDetails.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        Employee.append({
                "emp_id": int(row["emp_id"]),
                "name": row["name"],
                "department": row["department"],
                "salary": float(row["salary"])
            })
    for employee in Employee:
        if employee['emp_id'] == 218300:
                print(employee)
                break
        else:
                print("Employee Not Found")








# import gradio as gr
# from pyannote.audio import Pipeline

# # Load pipeline once (not inside function to save time)
# pipeline = Pipeline.from_pretrained(
#     "pyannote/speaker-diarization",
#     use_auth_token="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"
# )

# print(pipeline)

# def diarize_audio(audio_file):
#     diarization = pipeline(audio_file)

#     results = []
#     for turn, _, speaker in diarization.itertracks(yield_label=True):
#         results.append(f"Speaker {speaker} [{turn.start:.1f}s - {turn.end:.1f}s]")

#     return "\n".join(results)

# demo = gr.Interface(
#     fn=diarize_audio,
#     inputs=gr.Audio(sources=['microphone', 'upload'], type='filepath'),
#     outputs="text",
#     title="Speaker Diarization",
#     description="Upload a meeting recording and identify who spoke when."
# )

# demo.launch()
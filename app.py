from flask import Flask, request, jsonify
import io
from PIL import Image
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO('yolov8n.pt')

@app.route("/")
def home():
    html = f"<h3>Sklearn Prediction Home</h3>"
    return html.format(format)
@app.route("/objectdetection/", methods=["POST"])
def predict():
    if request.method != "POST":
        return

    if request.files.get("image"):
        image_file = request.files["image"]
        image_bytes = image_file.read()
        img = Image.open(io.BytesIO(image_bytes))
        results = model(img)
        results_json = {"boxes":results[0].boxes.xyxy.tolist(),"classes":results[0].boxes.cls.tolist()}
        object_classes = model.model.names

        output_list = list(map(lambda x: object_classes[int(x)], results_json["classes"]))

        return jsonify({"result": output_list})


if __name__ == "__main__":
    # load pretrained model as clf
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80

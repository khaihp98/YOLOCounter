import os

# ép load đúng DLL path sớm nhất có thể
onnx_path = os.path.join(os.path.dirname(__file__), "onnxruntime", "capi")
if os.path.exists(onnx_path):
    os.add_dll_directory(onnx_path)

# force import sớm
import onnxruntime
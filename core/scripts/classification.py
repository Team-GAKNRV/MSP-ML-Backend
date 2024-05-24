import torch
import cv2
import torchvision.transforms as transforms
import numpy as np
import joblib

from core.scripts.constants import PATH_LABELS
from core.scripts.loss_functions import loss_fn
from core.scripts.models import SingleHeadResNet50


def classify_single_label(model_path: str, layers_count: int, tag_name: str, input_image_path: str) -> str:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = SingleHeadResNet50(pretrained=False, requires_grad=False, layers=layers_count)
    checkpoint = torch.load(model_path, map_location=device)
    
    model.load_state_dict(checkpoint['model_state_dict'])
    model.to(device)
    model.eval()

    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    image = cv2.imread(input_image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = transform(image)
    image = image.unsqueeze(0).to(device)
    
    with torch.no_grad():
        output = model(image)
    
    out_label = np.argmax(output.cpu().numpy())
    num_list_data = joblib.load(f"{PATH_LABELS}/{tag_name}.pkl")

    data_keys = list(num_list_data.keys())
    data_values = list(num_list_data.values())
    
    final_label = data_keys[data_values.index(out_label)]
    
    return final_label

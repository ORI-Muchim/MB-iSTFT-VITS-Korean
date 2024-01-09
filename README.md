# MB-iSTFT-VITS

This is an implementation of [MB-iSTFT-VITS](https://github.com/MasayaKawamura/MB-iSTFT-VITS)
</br>

- Supported Language: Korean

## Table of Contents 
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Create transcript](#create-transcript)
- [Preprocess](#preprocess)
- [Training](#training)
- [References](#references)


## Prerequisites
- A Windows/Linux system with a minimum of `16GB` RAM.
- A GPU with at least `12GB` of VRAM.
- Python == 3.8
- Anaconda installed.
- PyTorch installed.
- CUDA 11.x installed.
- Zlib DLL installed.

Pytorch install command:
```sh
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
```

CUDA 11.7 install:
`https://developer.nvidia.com/cuda-11-7-0-download-archive`

Zlib DLL install:
`https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-zlib-windows`

---


## Installation 
1. **Create an Anaconda environment:**

```sh
conda create -n vits python=3.8
```

2. **Activate the environment:**

```sh
conda activate vits
```

3. **Clone this repository to your local machine:**

```sh
git clone https://github.com/ORI-Muchim/MB-iSTFT-VITS-Korean.git
```

4. **Navigate to the cloned directory:**

```sh
cd MB-iSTFT-VITS-Korean
```

5. **Install the necessary dependencies:**

```sh
pip install -r requirements.txt
```


## Create transcript
### Single speaker
"n_speakers" should be 0 in config.json
```
path/to/XXX.wav|transcript
```
- Example
```
dataset/001.wav|こんにちは。
```

### Mutiple speakers
Speaker id should start from 0 
```
path/to/XXX.wav|speaker id|transcript
```
- Example
```
dataset/001.wav|0|こんにちは。
```


## Preprocess
```sh
# Single speaker
python preprocess.py --text_index 1 --filelists path/to/filelist_train.txt path/to/filelist_val.txt --text_cleaners 'korean_cleaners'

# Mutiple speakers
python preprocess.py --text_index 2 --filelists path/to/filelist_train.txt path/to/filelist_val.txt --text_cleaners 'korean_cleaners'
```

If your speech file is either not `Mono / PCM-16`, the you should resample your .wav file first. 


## Setting json file in [configs](configs)

| Model | How to set up json file in [configs](configs) | Sample of json file configuration|
| :---: | :---: | :---: |
| iSTFT-VITS | ```"istft_vits": true, ```<br>``` "upsample_rates": [8,8], ``` | ljs_istft_vits.json |
| MB-iSTFT-VITS | ```"subbands": 4,```<br>```"mb_istft_vits": true, ```<br>``` "upsample_rates": [4,4], ``` | ljs_mb_istft_vits.json |
| MS-iSTFT-VITS | ```"subbands": 4,```<br>```"ms_istft_vits": true, ```<br>``` "upsample_rates": [4,4], ``` | ljs_ms_istft_vits.json |

- If you have done preprocessing, set "cleaned_text" to true. 
- Change `training_files` and `validation_files` to the path of preprocessed manifest files. 
- Select same `text_cleaners` you used in preprocessing step. 

## Training
```sh
# Single speaker
python train.py -c <config> -m <folder>

# Mutiple speakers
python train_ms.py -c <config> -m <folder>
```
Resume training from lastest checkpoint is automatic.

After the training, you can check inference audio using [inference.ipynb](inference.ipynb)

OR, Check [inference_cpu.py](inference_cpu.py)

```sh
python inference_cpu.py {model_name} {model_step}
```

## References
- [MasayaKawamura/MB-iSTFT-VITS](https://github.com/MasayaKawamura/MB-iSTFT-VITS)
- [misakiudon/MB-iSTFT-VITS-multilingual](https://github.com/misakiudon/MB-iSTFT-VITS-multilingual)
- [CjangCjengh/vits](https://github.com/CjangCjengh/vits)
- [Francis-Komizu/VITS](https://github.com/Francis-Komizu/VITS)
- [ORI-Muchim/PolyLangVITS](https://github.com/ORI-Muchim/PolyLangVITS)

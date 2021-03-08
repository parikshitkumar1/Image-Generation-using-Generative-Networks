---

# Durer
## Motivation
To create a web app based on WGAN-GP that generates realistic paintings of Albrecht Dürer
## Requirements
Python 3.8 or above with all [requirements](requirements.txt) dependencies installed. To install run:
```python
$ pip3 install -r requirements.txt
```
## To run
```python
$ streamlit run durer.py
```
>>or check it out here: 

## Architecture and other details

#### Trained for nearly 150 epochs on approximately 8000 paintings of Albrecht Dürer

<img src="https://user-images.githubusercontent.com/52780573/110354770-8a452300-805e-11eb-817c-3045e33b536a.gif" data-canonical-src="" width="800" height="500" />


#### w1 ---> weights saved at 100 epochs, w2 ---> weights saved at 150 epochs, total epochs ~150

## Results

#### finals scores: loss_g: 0.5128, loss_d: 1.1873, real_score: 0.5859, fake_score: 0.0469

<img src="https://user-images.githubusercontent.com/52780573/110355252-07709800-805f-11eb-8816-7e07103fad94.png" data-canonical-src="" width="500" height="350" />


<img src="https://user-images.githubusercontent.com/52780573/110355448-3f77db00-805f-11eb-80d1-d853d1e4140a.png" data-canonical-src="" width="500" height="350" />



## Might Do
- [ ] Upload WGAN-GP Notebook

---

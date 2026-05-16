# KS-OPTIMISER

output screenshots 
<img width="1900" height="1001" alt="Screenshot 2026-05-16 170841" src="https://github.com/user-attachments/assets/7e8aadd9-1e5c-4362-b3d2-eb558acf6913" />
<img width="1896" height="1020" alt="Screenshot 2026-05-16 170905" src="https://github.com/user-attachments/assets/4af58376-8443-42ba-a1c4-480138e16046" />

inside cmd run 
setup instructions-

1. git clone https://github.com/satishdahare88/KS-OPTIMISER.git
2. cd KS-OPTIMISER

in windows-
3. python -m venv venv
4. venv\Scripts\activate
in mac or linux-
5. python3 -m venv venv,
6. source venv/bin/activate,
7. pip install -r requirements.txt
8. uvicorn app.main:app 

with docker -
1. docker build -t ks-optimizer .
2. docker run -p 8000:8000 ks-optimizer


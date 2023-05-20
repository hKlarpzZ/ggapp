@echo off

call %~dp0..\venv\Scripts\activate

uvicorn gg_api:app --reload
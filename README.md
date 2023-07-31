# PDF_to_Json_convertor
PDF_to_Json_convertor for making LLM dataset
KoAlpaca의 fine-tuninig을 위해 만든 PDF -> Json 변환코드.

```
pip install -r requirements.txt
```

# 사용법 
1. 변환하고자 하는 PDF를 */pdf/* 안에 넣는다
2. ```python3 pdf_to_json_converter.py``` 를 사용해 변환.
3. */json/* 에서 변환결과 확인


soynlp기반 한국어 tokenizer인 konlpy를 사용해서 단어를 parsing.

PDF의 각 Page별로 읽을 수 있는 모든 text를 한개의 *{'text': 'your_contents'}* 로 변환.

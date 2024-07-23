## Một số references quan trọng cho các em
[1] A. Ushio, F. Alva-Manchego, and J. Camacho-Collados, “A Practical Toolkit for Multilingual Question and Answer Generation,” in Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations), D. Bollegala, R. Huang, and A. Ritter, Eds., Toronto, Canada: Association for Computational Linguistics, Jul. 2023, pp. 86–94. doi: 10.18653/v1/2023.acl-demo.8. Access here: (https://aclanthology.org/2023.acl-demo.8/)

[2] L. Phan, H. Tran, H. Nguyen, and T. H. Trinh, “ViT5: Pretrained Text-to-Text Transformer for Vietnamese Language Generation,” in Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies: Student Research Workshop, D. Ippolito, L. H. Li, M. L. Pacheco, D. Chen, and N. Xue, Eds., Hybrid: Seattle, Washington + Online: Association for Computational Linguistics, Jul. 2022, pp. 136–142. doi: 10.18653/v1/2022.naacl-srw.18.Access here: (https://aclanthology.org/2022.naacl-srw.18/)

[3] “mrm8488/t5-base-finetuned-question-generation-ap · Hugging Face.” Accessed: Jul. 23, 2024. [Online]. Available: https://huggingface.co/mrm8488/t5-base-finetuned-question-generation-ap

[4] S. Patil, Question Generation using transformers. (Jul. 22, 2024). Jupyter Notebook. Accessed: Jul. 23, 2024. [Online]. Available: https://github.com/patil-suraj/question_generation

## Gợi ý một số cách đặt tên
1. **Tích hợp RAG và GPT-3.5 trong việc tạo câu hỏi và trả lời: Một nghiên cứu thực nghiệm**
2. **Phát triển hệ thống hỏi đáp thông minh sử dụng RAG và GPT-3.5: Thực tiễn và thách thức**
3. **Ứng dụng mô hình RAG và GPT-3.5 trong giáo dục: Tạo câu hỏi và trả lời tự động**
4. **Nâng cao hiệu quả hỏi đáp với RAG và GPT-3.5: Kỹ thuật và kết quả**
5. **Sự kết hợp giữa RAG và GPT-3.5: Phương pháp tạo câu hỏi và trả lời thông minh**
6. **Phân tích hiệu suất của RAG và GPT-3.5 trong việc tạo hỏi đáp tự động**
7. **Khám phá tiềm năng của RAG và GPT-3.5 trong hệ thống hỏi đáp**
8. **Tích hợp RAG và GPT-3.5 cho các ứng dụng hỏi đáp: Một hướng dẫn toàn diện**
9. **Cải thiện trải nghiệm người dùng trong các hệ thống hỏi đáp bằng RAG và GPT-3.5**
10. **Ứng dụng RAG và GPT-3.5 trong tạo câu hỏi và trả lời cho hệ thống hỗ trợ học tập**

## Dàn ý để viết paper:
- tiêu đề 
- cơ sở lý thuyết
   - aqg
   - llm
- đề xuất mô hình
- cách đánh giá:
   - Độ đo ROUGE: nên dùng L hoặc N
   - Cài đặt thực nghiệm: so sánh mô hình của nhóm và 1 LLM khác / 1 công trình khác (mới nhất) có thể làm được việc này
   - Độ đo ROUGE cho kết quả tốt hơn thì công bố
   - Để đo được ROUGE: thì các em cần 1 dataset chuẩn để làm cơ sở so sánh (ví dụ: vietnews tuy nhiên đây là trang tin tức, nên khi so sánh với bối cảnh của chúng ta là bài giảng thì có hơi chưa trùng => tạm chấp nhận)




Đánh giá bài toán sinh câu hỏi trắc nghiệm tự động (Automatic Question Generation - AQG) đòi hỏi sử dụng các độ đo khác nhau để đảm bảo rằng các câu hỏi được sinh ra có chất lượng và phù hợp với mục tiêu giáo dục. Một số độ đo phổ biến được sử dụng bao gồm:

### 1. **Độ chính xác (Accuracy)**
   - **Precision**: Tỷ lệ câu hỏi được sinh ra đúng với ngữ cảnh và nội dung của tài liệu gốc.
   - **Recall**: Tỷ lệ các ý chính trong tài liệu gốc mà các câu hỏi sinh ra đã bao quát.
   - **F1-score**: Trung bình điều hòa của Precision và Recall.

### 2. **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**
   - **ROUGE-N**: Đo lường mức độ trùng lặp của các n-gram giữa câu hỏi sinh ra và câu hỏi chuẩn.
   - **ROUGE-L**: Đo lường độ dài của chuỗi con chung dài nhất (LCS) giữa câu hỏi sinh ra và câu hỏi chuẩn.

### 3. **BLEU (Bilingual Evaluation Understudy)**
   - Đo lường mức độ trùng lặp của các n-gram giữa câu hỏi sinh ra và câu hỏi chuẩn, chủ yếu được sử dụng trong dịch máy nhưng cũng có thể áp dụng cho AQG.

### 4. **METEOR (Metric for Evaluation of Translation with Explicit ORdering)**
   - Đo lường sự tương đồng về từ vựng, hình thái học, và ngữ nghĩa giữa câu hỏi sinh ra và câu hỏi chuẩn.

### 5. **Diversity Measures**
   - **Lexical Diversity**: Đánh giá sự đa dạng về từ vựng trong các câu hỏi sinh ra.
   - **Syntactic Diversity**: Đánh giá sự đa dạng về cấu trúc ngữ pháp trong các câu hỏi sinh ra.

### 6. **Human Evaluation**
   - **Relevance**: Mức độ liên quan của câu hỏi với tài liệu gốc.
   - **Fluency**: Mức độ mạch lạc và dễ hiểu của câu hỏi.
   - **Difficulty**: Mức độ khó của câu hỏi, đảm bảo phù hợp với trình độ người học.
   - **Educational Value**: Đánh giá khả năng của câu hỏi trong việc kiểm tra và củng cố kiến thức của người học.

### 7. **Automatic Evaluation Metrics**
   - **QG-specific metrics**: Một số thước đo tự động được phát triển đặc biệt cho việc đánh giá AQG như Q-metric, có thể đo lường tính hiệu quả của câu hỏi trong việc kiểm tra kiến thức cụ thể.

### 8. **Item Response Theory (IRT)**
   - Sử dụng mô hình thống kê để đánh giá chất lượng câu hỏi dựa trên phản hồi của người học, giúp xác định độ khó và khả năng phân biệt của câu hỏi.

### Tổng Kết
Sử dụng kết hợp các độ đo tự động và đánh giá từ chuyên gia là cách tiếp cận tốt nhất để đánh giá chất lượng của các câu hỏi trắc nghiệm được sinh ra tự động. Điều này đảm bảo rằng các câu hỏi không chỉ chính xác và liên quan mà còn phù hợp với mục tiêu giáo dục và người học.

-----------------------------
ROUGE (Recall-Oriented Understudy for Gisting Evaluation) là một bộ các thước đo đánh giá tóm tắt văn bản tự động và dịch máy. ROUGE chủ yếu sử dụng để so sánh văn bản được tạo ra bởi máy với một hoặc nhiều văn bản chuẩn do con người viết. Các thước đo phổ biến trong ROUGE bao gồm:

1. **ROUGE-N**: Đánh giá dựa trên sự trùng lặp của n-gram giữa tóm tắt do máy tạo ra và tóm tắt chuẩn.
   - **ROUGE-1**: Sử dụng đơn từ (unigram).
   - **ROUGE-2**: Sử dụng cặp từ liên tiếp (bigram).
   - **ROUGE-3**: Sử dụng bộ ba từ liên tiếp (trigram), và có thể tiếp tục cho các n lớn hơn.

2. **ROUGE-L**: Đánh giá dựa trên độ dài của chuỗi con chung dài nhất (Longest Common Subsequence - LCS) giữa tóm tắt do máy tạo ra và tóm tắt chuẩn. ROUGE-L có thể nắm bắt được cấu trúc chuỗi và thứ tự từ trong văn bản.

3. **ROUGE-W**: Biến thể của ROUGE-L, nhưng cho trọng số lớn hơn cho các chuỗi con chung dài hơn, giúp đánh giá chính xác hơn sự liên tục của các từ trong văn bản.

4. **ROUGE-S**: Đánh giá dựa trên sự trùng lặp của các cặp từ không liên tiếp (skip-bigram) với một khoảng cách cố định giữa các từ.

5. **ROUGE-SU**: Kết hợp giữa skip-bigram và unigram, cung cấp đánh giá toàn diện hơn.

Các chỉ số của ROUGE thường được tính toán dựa trên ba thành phần chính:
- **Precision (P)**: Tỷ lệ các n-gram trong tóm tắt do máy tạo ra xuất hiện trong tóm tắt chuẩn.
- **Recall (R)**: Tỷ lệ các n-gram trong tóm tắt chuẩn xuất hiện trong tóm tắt do máy tạo ra.
- **F1-score**: Trung bình điều hòa của Precision và Recall, cung cấp một thước đo cân bằng giữa hai yếu tố này.

ROUGE được sử dụng rộng rãi trong nghiên cứu và ứng dụng về xử lý ngôn ngữ tự nhiên (NLP), đặc biệt là trong các hệ thống tóm tắt văn bản tự động, để đánh giá chất lượng và hiệu quả của các thuật toán.

---------------------------
Để cài đặt và sử dụng độ đo ROUGE (Recall-Oriented Understudy for Gisting Evaluation) trên một tập dữ liệu đã cho, bạn có thể làm theo các bước sau. Dưới đây là hướng dẫn chi tiết bằng Python sử dụng thư viện `rouge-score`.

### Bước 1: Cài đặt Thư viện
Trước tiên, bạn cần cài đặt thư viện `rouge-score` nếu chưa cài đặt.

```bash
pip install rouge-score
```

### Bước 2: Chuẩn bị Dữ liệu
Giả sử bạn có một tập dữ liệu gồm các câu tóm tắt (summary) và các câu gốc (reference). Bạn cần chuẩn bị dữ liệu dưới dạng các danh sách.

```python
references = [
    "This is the reference summary for document one.",
    "This is the reference summary for document two."
    # Thêm các câu gốc khác
]

summaries = [
    "This is the generated summary for document one.",
    "This is the generated summary for document two."
    # Thêm các câu tóm tắt khác
]
```

### Bước 3: Tính Toán Độ Đo ROUGE
Bạn có thể sử dụng thư viện `rouge-score` để tính toán các độ đo ROUGE (ROUGE-1, ROUGE-2, ROUGE-L).

```python
from rouge_score import rouge_scorer

# Tạo đối tượng tính toán ROUGE
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

# Hàm tính toán ROUGE cho các cặp reference và summary
def compute_rouge(references, summaries):
    scores = {'rouge1': [], 'rouge2': [], 'rougeL': []}
    for ref, summary in zip(references, summaries):
        score = scorer.score(ref, summary)
        for key in scores:
            scores[key].append(score[key].fmeasure)
    return scores

# Tính toán ROUGE
rouge_scores = compute_rouge(references, summaries)

# Tính trung bình cho từng độ đo ROUGE
average_rouge_scores = {key: sum(value) / len(value) for key, value in rouge_scores.items()}
print(average_rouge_scores)
```

### Kết Quả
Kết quả sẽ là một từ điển chứa các giá trị trung bình của các độ đo ROUGE-1, ROUGE-2 và ROUGE-L cho toàn bộ tập dữ liệu của bạn.

```python
print("ROUGE-1:", average_rouge_scores['rouge1'])
print("ROUGE-2:", average_rouge_scores['rouge2'])
print("ROUGE-L:", average_rouge_scores['rougeL'])
```

### Ghi chú
- `use_stemmer=True`: sử dụng bộ tiền xử lý stemming để so khớp các từ gốc.
- Bạn có thể tùy chỉnh cách tính toán hoặc thêm các độ đo ROUGE khác nếu cần.

### Ví dụ đầy đủ

```python
from rouge_score import rouge_scorer

# Danh sách các câu gốc và câu tóm tắt
references = [
    "This is the reference summary for document one.",
    "This is the reference summary for document two."
    # Thêm các câu gốc khác
]

summaries = [
    "This is the generated summary for document one.",
    "This is the generated summary for document two."
    # Thêm các câu tóm tắt khác
]

# Tạo đối tượng tính toán ROUGE
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

# Hàm tính toán ROUGE cho các cặp reference và summary
def compute_rouge(references, summaries):
    scores = {'rouge1': [], 'rouge2': [], 'rougeL': []}
    for ref, summary in zip(references, summaries):
        score = scorer.score(ref, summary)
        for key in scores:
            scores[key].append(score[key].fmeasure)
    return scores

# Tính toán ROUGE
rouge_scores = compute_rouge(references, summaries)

# Tính trung bình cho từng độ đo ROUGE
average_rouge_scores = {key: sum(value) / len(value) for key, value in rouge_scores.items()}

# In kết quả
print("ROUGE-1:", average_rouge_scores['rouge1'])
print("ROUGE-2:", average_rouge_scores['rouge2'])
print("ROUGE-L:", average_rouge_scores['rougeL'])
```

Hy vọng hướng dẫn này sẽ giúp bạn cài đặt và sử dụng độ đo ROUGE cho tập dữ liệu của mình. Nếu bạn có thêm câu hỏi hoặc cần hỗ trợ thêm, hãy cho mình biết!

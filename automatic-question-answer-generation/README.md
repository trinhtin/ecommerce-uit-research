Dàn ý để viết paper:
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

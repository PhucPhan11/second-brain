---
title: Token Tax (thiên lệch tokenizer theo ngôn ngữ)
tags: [tokenization, llm-cost, multilingual, fairness]
sources:
  - "[[ai/sources/the-batch/2026-11-27]]"
updated: 2026-11-27
---

# Token Tax (thiên lệch tokenizer theo ngôn ngữ)

## Tóm tắt
Tokenizer tạo token dựa trên tần suất các chuỗi ký tự trong dữ liệu train. Ngôn ngữ ít dữ liệu, nhất là ngôn ngữ dùng chữ viết ít phổ biến, bị cắt thành nhiều mảnh nhỏ. Kết quả là **cùng một nội dung tốn nhiều token hơn**, nên đắt hơn, chậm hơn và thường chất lượng kém hơn. Đây là một "thuế" vô hình đánh lên người dùng không nói tiếng Anh.

## Chi tiết / số liệu
Nghiên cứu của **CLEAR** (Coalition for Language Equity in AI Research):
- Ngôn ngữ bị phục vụ kém nhất tốn tới **17×** token so với ngôn ngữ được phục vụ tốt nhất.
- Cùng một câu trên GPT-5: tiếng Anh **13** token, Malayalam **26**, Amharic **78**, dù số ký tự gần như nhau.
- Đo trên **FLORES-200** (204 cặp ngôn ngữ–chữ viết), chấm theo tỉ lệ max/min số token: **A** khi ≤3×, **F** khi >12×.
  - GPT-5 và Llama 3.3: **F**
  - Gemini/Gemma: **B** (điểm tốt nhất)
  - Qwen 3.6: 13.1×, còn Qwen 3 cũ hơn chỉ 10.5×. **Model mới chưa chắc tốt hơn.**

Các nghiên cứu trước:
- Petrov et al. (NeurIPS 2023): chênh lệch tới **15×**, còn làm chậm inference.
- Ahia et al. (2023): 22 ngôn ngữ trên API OpenAI, bị tính giá cao hơn mà kết quả kém hơn.
- Nghiên cứu 2024 về GPT-4o: tokenizer có nhiều token tiếng Trung rất dài lấy từ spam, cờ bạc và nội dung người lớn, khiến model xử lý chúng kém hơn GPT-4.

## Ví dụ / biến thể
- **Hệ quả kinh tế:** startup và người dùng ở thị trường mới nổi vốn đã thiếu hạ tầng, nay còn chịu thêm chi phí token.
- **Hệ quả văn hoá:** người dùng bị đẩy sang chữ Latin hoặc ngôn ngữ lớn (tiếng Anh, tiếng Trung), dẫn tới đơn văn hoá ngôn ngữ.
- **Hướng khắc phục:** tokenizer tốt hơn cho ngôn ngữ ít dữ liệu, kết hợp nghiên cứu văn bản và dân tộc học về ngôn ngữ đó.

## Áp dụng cho mình
- **Tiếng Việt** dùng chữ Latin nhưng có nhiều dấu, nên chi phí token có thể cao hơn tiếng Anh. Newsletter không có số liệu cho tiếng Việt, đây là điều cần tự kiểm chứng.
- Ý tưởng thử nghiệm: lấy cùng một đoạn văn bằng tiếng Anh và tiếng Việt, đếm token bằng token counter của từng model (Claude, GPT, Gemini), rồi ghi tỉ lệ vào note này.
- Khi làm app hoặc prompt dài: viết system prompt/instruction bằng tiếng Anh để tiết kiệm token, còn output thì để tiếng Việt cho người dùng.
- Khi chọn model cho nội dung tiếng Việt, tính cả hiệu quả tokenizer vào chi phí thực, không chỉ so đơn giá.

## Nguồn
- [[ai/sources/the-batch/2026-11-27]] (mục 3: "Token Tax")
- [CLEAR: The Tokenizer Tax](https://clear-languages.org/blog/the-tokenizer-tax) · [FLORES-200](https://github.com/facebookresearch/flores/blob/main/flores200/README.md) · [Petrov et al. 2023](https://arxiv.org/abs/2305.15425) · [Ahia et al. 2023](https://arxiv.org/abs/2305.13707) · [Nghiên cứu tokenizer GPT-4o 2024](https://arxiv.org/html/2406.11214v2)

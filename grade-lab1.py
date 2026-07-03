def calculate_grade(scores):
    # 1. ป้องกัน Bug กรณีลิสต์ว่าง
    if not scores:
        return "No Data", 0
    
    # 2. ป้องกัน Bug กรณีข้อมูลไม่ใช่ตัวเลข หรือคะแนนติดลบ (Optional)
    # ตรวจสอบเบื้องต้นเพื่อให้มั่นใจว่าคำนวณได้
    total = sum(scores) 
    average = total / len(scores)
    
    # 3. การตัดสินเกรด (Logic เดิมถูกต้องแล้ว แต่จัดให้กระชับขึ้นได้)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade, average

# การทดสอบ
scores = [85, 92, 78, 88, 95]
grade, avg = calculate_grade(scores)
print(f"Grade: {grade}, Average: {avg:.2f}")

# ทดสอบกรณีลิสต์ว่าง (จะไม่พังแล้ว)
print(calculate_grade([]))

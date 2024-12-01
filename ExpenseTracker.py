import os
import click
import csv
import calendar
from datetime import datetime

file_path = r"D:\code\roadmap project py\Expense Tracker\data.csv"
if not os.path.exists(file_path):
    with open(file_path, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Date", "Description", "Amount"])
        id=0
    print(f"File '{file_path}' created.")

def get_next_id():
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        return 1  # Nếu file trống hoặc không tồn tại, bắt đầu từ 1
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua tiêu đề
        ids = [int(row[0]) for row in reader if row]  # Lấy cột ID
        return max(ids) + 1 if ids else 1  # ID tiếp theo
    
@click.group()
def expense_tracker():
    """Expense Tracker CLI"""
    pass
@expense_tracker.command()
@click.option("--description", required = True, help="Description of the expense")
@click.option("--amount",required = True, help = "amount of the expense")
def add(description, amount):
    with open(file_path, "a", newline='') as file:
        id=get_next_id()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer = csv.writer(file)
        writer.writerow([id,date,description,amount])
    click.echo(f"Expense added successfully (ID: {id})")

@expense_tracker.command()
@click.option("--id", required=True, help="ID of the expense")
@click.option("--new-description", required=False, help="New description of the expense")
@click.option("--new-amount", required=False, help="New amount of the expense")
def update(id,new_description=None,new_amount=None):
    updating=False
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)  # Đọc toàn bộ dữ liệu thành danh sách
    for i,row in enumerate(rows):
        if i==0:
            continue
        if int(row[0]) == id:
            if new_description:
                row[2]=new_description
                row[1]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")   
            if new_amount:
                row[3]=new_amount
                row[1]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            rows[i] = row
            updating=True      
            break 
    if updating:
        with open(file_path, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        click.echo(f"ID {id} was updated successfully")
    else:
        click.echo(f"ID {id} was not found")

def reset_id():
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)  # Đọc toàn bộ dữ liệu

    # Kiểm tra nếu file chỉ có tiêu đề hoặc rỗng
    if len(rows) <= 1:
        print("No data to reset IDs.")
        return

    # Cập nhật lại ID cho từng hàng (bỏ qua tiêu đề)
    updated_rows = [rows[0]]  # Giữ lại tiêu đề
    for new_id, row in enumerate(rows[1:], start=1):
        row[0] = str(new_id)  # Cập nhật ID
        updated_rows.append(row)

    # Ghi lại file với ID đã cập nhật
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

@expense_tracker.command()
@click.option("--id",required=True, type=int, help="ID of the expense to delete")
def delete(id):
    deleted = False
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)  # Đọc toàn bộ dữ liệu thành danh sách

    # Duyệt từng hàng và xóa hàng có ID khớp
    updated_rows = [rows[0]]  # Giữ lại tiêu đề
    for row in rows[1:]:  # Bỏ qua tiêu đề
        if int(row[0]) == id:
            deleted = True
        else:
            updated_rows.append(row)

    # Ghi lại file nếu có thay đổi
    if deleted:
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        reset_id()    
        click.echo(f"ID {id} was deleted.")
    else:
        click.echo(f"ID {id} was not found.")

@expense_tracker.command(name="show")
def show():
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        if len(rows) < 2:  # Nếu chỉ có tiêu đề hoặc rỗng
            click.echo("No expenses to show.")
            return

        click.echo(f"{rows[0][0]:<5} {rows[0][1]:<20} {rows[0][2]:<15} {rows[0][3]:<10}")
        click.echo("-" * 50)

        for row in rows[1:]:
            click.echo(f"{row[0]:<5} {row[1]:<20} {row[2]:<15} {row[3]:<10}")
    except Exception as e:
        click.echo(f"Error: {e}")
def Total():
      with open(file_path,"r") as file:
        reader = csv.reader(file)
        rows=list(reader)
      sumed=0  
      for row in rows[1:]:
          sumed=sumed+int(row[3])
      return sumed

def Total_of_month(month):
    with open(file_path,"r") as file:
        reader = csv.reader(file)
        rows=list(reader)
    summed=0
    for row in rows[1:]:
        row_date = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")  # Chuyển đổi chuỗi thành datetime
        if row_date.month == month:
            summed = summed + int(row[3])
    return summed
@expense_tracker.command()
@click.option("--month", required=False, type=int, help="Filter by month (1-12)")
def summary(month):
    if month:
        tong = Total_of_month(month)
        click.echo(f"Total expenses for {calendar.month_name[month]}: ${tong}")
    else:
        tong = Total()
        click.echo(f"Total expenses: ${tong}")

if __name__ == "__main__":
    expense_tracker()      
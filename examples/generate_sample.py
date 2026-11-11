"""Recreate the synthetic workbook; contains no importer functionality."""

from pathlib import Path

from openpyxl import Workbook


def main():
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Sản phẩm mẫu"
    rows = [
        ["Mã hàng", "Tên hàng", "Thương hiệu", "Giá bán", "Mô tả"],
        ["DEMO-FR100-A", "Tủ lạnh ExampleCool DEMO-FR100-A", "ExampleCool",
         10700000, "TẶNG BÌNH GIỮ NHIỆT MẪU\nHOẶC TẶNG ẤM ĐUN MẪU"],
        ["DEMO-WM200-B", "Máy giặt ExampleWash DEMO-WM200-B", "ExampleWash",
         5200000, None],
        ["DEMO-TV300-C", "Tivi ExampleView DEMO-TV300-C", "ExampleView",
         0, "KHÔNG ÁP DỤNG: DÒNG GIÁ BẰNG KHÔNG"],
        ["DEMO-AC400-D", "Máy lạnh ExampleAir DEMO-AC400-D", "ExampleAir",
         -100, None],
        ["DEMO-OV500-E", "Lò nướng ExampleHeat DEMO-OV500-E", "ExampleHeat",
         "invalid", None],
    ]
    for row in rows:
        sheet.append(row)
    workbook.save(Path(__file__).with_name("sample_products.xlsx"))
    workbook.close()


if __name__ == "__main__":
    main()

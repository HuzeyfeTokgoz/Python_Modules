# Python_Modules

Temel sözdiziminden fonksiyonel programlamaya uzanan 11 modüllük Python
alıştırma serisi. Her modül kendi temasına sahip bir senaryo (bahçe, oyun,
siber arşiv, simya, Matrix, uzay istasyonu, büyücülük) üzerinden tek bir
konuyu işler ve `exN/` klasörleri halinde alıştırmalara bölünür.

## Gereksinimler

- **Python 3.10+** — kodda `str | None` gibi birleşim tipleri ve
  `list[str]` / `dict[str, int]` gibi yerleşik jenerikler kullanılıyor.
- Modül 8 ve 9 için ek paketler (aşağıdaki [Bağımlılıklar](#bağımlılıklar)
  bölümüne bakın). Diğer tüm modüller yalnızca standart kütüphaneyi kullanır.

Kod, `flake8` (79 karakter satır sınırı) ve `mypy` denetimlerinden geçecek
şekilde yazılmıştır; fonksiyonlar tip imzalarıyla birlikte tanımlanır.

## Modüller

| Modül | Tema | Konu |
| --- | --- | --- |
| [python_module_0](python_module_0/) | Garden | Temeller: `input`, biçimli çıktı, `if/else`, döngüler, özyineleme, fonksiyon parametreleri |
| [python_module_1](python_module_1/) | Garden | OOP: sınıflar, metotlar, kapsülleme (getter/setter), kalıtım (`Flower`, `Tree`), iç içe sınıf ve isim bozma (`__` ile sayaç tutma) |
| [python_module_2](python_module_2/) | Garden | Hata yönetimi: `try/except`, `raise`, farklı hata tipleri, özel hata hiyerarşisi (`GardenError` → `PlantError`/`WaterError`), `finally` |
| [python_module_3](python_module_3/) | Game | Veri yapıları: `sys.argv`, liste/demet/küme/sözlük işlemleri, üreteçler (`yield`), kapsam ifadeleri (comprehension) |
| [python_module_4](python_module_4/) | Cyber Archives | Dosya işlemleri: `open`/`read`/`close`, yazma, `stdout`/`stderr` ayrımı, `with` ve güvenli sarmalayıcı (`secure_archive`) |
| [python_module_5](python_module_5/) | Data Pipeline | Soyut sınıflar (`ABC`, `@abstractmethod`), çok biçimlilik, veri akışı kaydı ve CSV/JSON çıktı eklentileri |
| [python_module_6](python_module_6/) | Alchemy | Modül ve paket sistemi: `import` biçimleri, `__init__.py`, alt paketler, `__all__`, döngüsel içe aktarma sorunu |
| [python_module_7](python_module_7/) | Creatures | Tasarım desenleri: Abstract Factory, yetenek arayüzleri (`HealCapability`, `TransformCapability`), Strategy ve bunları birleştiren turnuva |
| [python_module_8](python_module_8/) | Matrix | Ortam yönetimi: sanal ortam algılama, `requirements.txt`/Poetry, `importlib` ile bağımlılık kontrolü, `.env` ve `python-dotenv` |
| [python_module_9](python_module_9/) | Space | Pydantic ile doğrulama: `BaseModel`, `Field` kısıtları, `Enum`, `model_validator`, CSV/JSON verisinin doğrulanması |
| [python_module_10](python_module_10/) | FuncMage | Fonksiyonel programlama: `lambda`, `map`/`filter`/`sorted`, üst düzey fonksiyonlar, kapanışlar (closure) ve kapsam |

## Çalıştırma

Alıştırmaların çoğu doğrudan çalıştırılabilir:

```bash
python3 python_module_1/ex1/ft_garden_data.py
python3 python_module_3/ex1/ft_score_analytics.py 42 17 abc 99
python3 python_module_4/ex0/ft_ancient_text.py bir_dosya.txt
```

Bazı modüller kendi dizininden çalıştırılmalıdır:

```bash
# Modül 6 — betikler hem üst düzey elements.py'yi hem alchemy paketini içe aktarır
cd python_module_6 && python3 ft_alembic_0.py

# Modül 7 — ex0/ex1/ex2 paketleri modül kökünden içe aktarılır
cd python_module_7 && python3 battle.py      # Abstract Factory
cd python_module_7 && python3 capacitor.py   # yetenek arayüzleri
cd python_module_7 && python3 tournament.py  # hepsi birlikte

# Modül 9 — veri dosyaları generated_data/ altından göreli yolla okunur
cd python_module_9 && python3 ex0/space_station.py
```

### Modüle özel notlar

- **python_module_0:** Dosyalar `__main__` bloğu içermez, yalnızca fonksiyon
  tanımlarından oluşur. İlgili klasörden içe aktarıp çağırarak deneyin:

  ```bash
  cd python_module_0/ex7
  python3 -c "from ft_seed_inventory import ft_seed_inventory as f
  f('tomato', 5, 'packets')"
  ```
- **python_module_6:** `ft_alembic_4.py` ve `ft_kaboom_1.py` **bilinçli olarak
  hata verir.** İlki `alchemy/__init__.py` içinde dışa aktarılmayan
  `create_earth`'e erişmeye çalışır; ikincisi `dark_spellbook` ile
  `dark_validator` arasındaki döngüsel içe aktarmaya düşer. Aynı yapının
  çalışan hâli `light_spellbook` tarafında, içe aktarmanın fonksiyon içine
  taşınmasıyla çözülmüştür.
- **python_module_8/ex0:** `construct.py`, sanal ortam içinde ve dışında
  farklı çıktı verir; her iki durumu da deneyin.
- **python_module_8/ex2:** Çalıştırmadan önce `.env.example` dosyasını `.env`
  olarak kopyalayın.
- **python_module_9:** Veri üretici arşiv olarak saklanır
  (`data_generator.tar`); üretilmiş veriler `generated_data/` altında depoya
  dahil edildiği için alıştırmaları çalıştırmak için arşivi açmanız gerekmez.
- **python_module_10:** `data_generator.py` (arşivi `generator.tar.gz`)
  alıştırmalar için hazır test verisi üreten yardımcı bir sınıf sunar;
  alıştırmalar kendi örnek verilerini içerdiği için zorunlu değildir.

## Bağımlılıklar

Standart kütüphane dışına çıkan tek yer modül 8 ve 9'dur. Sanal ortam içinde
kurmanız önerilir:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r python_module_8/ex1/requirements.txt   # pandas, numpy, matplotlib
pip install -r python_module_8/ex2/requirements.txt   # python-dotenv
pip install -r python_module_9/requirements.txt       # pydantic
```

`python_module_8/ex1` ayrıca Poetry ile de kurulabilir:

```bash
cd python_module_8/ex1 && poetry install
```

## Denetim

```bash
flake8 .
```

`mypy` için depo kökü yerine modül dizinlerini tek tek verin; farklı
modüllerde aynı adı taşıyan dosyalar (`elements.py`, `factories.py`) kökten
çalıştırıldığında modül adı çakışmasına yol açar:

```bash
cd python_module_7 && mypy .
```

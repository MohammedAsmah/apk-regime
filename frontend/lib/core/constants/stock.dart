part of index;


enum EntetyStock {
  session(String),
  themeMode(String);

  String get stockName {
    return 'stock_$name';
  }

  final Type type;
  const EntetyStock(this.type);
}

class StockState {
  SharedPreferences? _prefs;

  StockState() {
    _initPrefs();
  }

  _initPrefs() async {
    _prefs ??= await SharedPreferences.getInstance();
  }

  Future<bool> set(EntetyStock symbol, dynamic value) async {
    await _initPrefs();

    if (value == null) {
      await _prefs!.remove(symbol.stockName);
      return true;
    }

    switch (symbol.type) {
      case String:
        return await _prefs!.setString(symbol.stockName, value as String);
      case bool:
        return await _prefs!.setBool(symbol.stockName, value as bool);
      case int:
        return await _prefs!.setInt(symbol.stockName, value as int);
      case double:
        return await _prefs!.setDouble(symbol.stockName, value as double);
      case List:
        return await _prefs!
            .setStringList(symbol.stockName, value as List<String>);
      default:
        // throw Exception('Unsupported type');
        return await _prefs!.setString(symbol.stockName, jsonEncode(value));
    }
  }

  T? get<T>(EntetyStock symbol) {
    return _prefs!.get(symbol.stockName) as T?;
  }

  Future<bool> clear(EntetyStock symbol) async {
    return await _prefs?.remove(symbol.stockName) ?? false;
  }

  loadStock() async => await _initPrefs();
}


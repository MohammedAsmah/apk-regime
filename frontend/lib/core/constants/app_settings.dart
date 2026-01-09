part of index;


class SettingsState {
  final bool isLoading;
  final ThemeMode themeMode;
  final String? error;
  final bool hasMore;
  final int currentPage;

  const SettingsState({
    this.isLoading = false,
    this.error,
    this.themeMode = ThemeMode.light,
    this.hasMore = true,
    this.currentPage = 1,
  });

  SettingsState copyWith({
    bool? isLoading,
    List<Map<String, dynamic>>? emails,
    String? error,
    ThemeMode? themeMode,
    bool? hasMore,
    int? currentPage,
  }) {
    return SettingsState(
      isLoading: isLoading ?? this.isLoading,
      error: error,
      themeMode: themeMode ?? this.themeMode,
      hasMore: hasMore ?? this.hasMore,
      currentPage: currentPage ?? this.currentPage,
    );
  }
}

class SettingsProvider extends ChangeNotifier {
  final StockState stock;
  SettingsState _state = const SettingsState();
  SettingsState get state => _state;

  SettingsProvider(this.stock){
    ThemeMode savedThemeMode = ThemeMode.values.byName(stock.get<String>(EntetyStock.themeMode) ?? 'light');
    _state = _state.copyWith(themeMode: savedThemeMode);
    notifyListeners();
  }

  void clearError() {
    if (_state.error != null) {
      _state = _state.copyWith(error: null);
      notifyListeners();
    }
  }

  Future<void> toggleThemeMode()async {
    final newThemeMode = _state.themeMode == ThemeMode.dark
        ? ThemeMode.light
        : ThemeMode.dark;

    _state = _state.copyWith(themeMode: newThemeMode);
    
    await stock.set(EntetyStock.themeMode, newThemeMode.name);
    notifyListeners();
  }
}

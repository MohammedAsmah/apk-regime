import 'imports.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  final stock = StockState();
  await stock.loadStock();

  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(
          create: (_) => AuthProvider(),
        ),
        ChangeNotifierProvider(
          create: (_) => SettingsProvider(stock),
        ),
      ],
      child: TRNX(),
    ),
  );
}

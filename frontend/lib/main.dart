import 'imports.dart';
import 'package:flutter/material.dart';

// void main() {
//   runApp(const MyApp());
// }

// class MyApp extends StatelessWidget {
//   const MyApp({super.key});

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       debugShowCheckedModeBanner: false,
//       theme: ThemeData(
//         colorScheme: ColorScheme.fromSeed(seedColor: Color(0xFFF7F3EB)),
//       ),
//       home: WelcomePage(),
//     );
//   }
// }



void main() async {
  WidgetsFlutterBinding.ensureInitialized();


  final stock = StockState();
  await stock.loadStock();


  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(
          create: (_) => SettingsProvider(stock),
        ),
      ],
      builder: (context, child) {
        return GestureDetector(
          onTap: () {
            // (clear focus completely):
            FocusManager.instance.primaryFocus?.unfocus();
            FocusScope.of(context).requestFocus(FocusNode());
          },
          child: const TRNX(),
        );
      },
    ),
  );
}

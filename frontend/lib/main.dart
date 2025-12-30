import 'package:flutter/material.dart';
import 'package:flutter_trnx_project/pages/login_page.dart';
import 'package:flutter_trnx_project/pages/login_page.dart';
import 'package:flutter_trnx_project/pages/more_info_page.dart';
import 'package:flutter_trnx_project/pages/sign_up_page.dart';
import 'package:flutter_trnx_project/pages/welcome_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Color(0xFFF7F3EB)),
      ),
      home: SignUpPage(),
    );
  }
}

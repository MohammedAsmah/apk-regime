import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flutter_trnx_project/pages/login_page.dart';
import 'package:flutter_trnx_project/pages/more_info_page.dart';

class SignUpPage extends StatefulWidget {
  const SignUpPage({super.key});

  @override
  State<SignUpPage> createState() => _SignUpPageState();
}

class _SignUpPageState extends State<SignUpPage> {
  bool _obscureText = true;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: true,
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 40, horizontal: 31),
          child: SingleChildScrollView(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Text(
                  'create an account',
                  style: Theme.of(context).textTheme.headlineLarge!.copyWith(
                    fontWeight: FontWeight.w500,
                  ),
                ),
                // log in link
                RichText(
                  text: TextSpan(
                    style: Theme.of(context).textTheme.bodyLarge,
                    children: [
                      const TextSpan(text: 'Already have an account? '),
                      TextSpan(
                        text: 'Log in',
                        style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                          decoration: TextDecoration.underline,
                          color: Colors.black,
                          fontWeight: FontWeight.w500,
                        ),
                        recognizer: TapGestureRecognizer()
                          ..onTap = () {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) => LoginPage(),
                              ),
                            );
                          },
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 20),
                SizedBox(
                  width: 340,
                  child: Text(
                    'First name',
                    style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                      color: Theme.of(context).hintColor,
                    ),
                  ),
                ),
                const SizedBox(height: 12),
                SizedBox(
                  width: 340,
                  child: TextField(
                    decoration: InputDecoration(
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12),
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 26),
                // last name textFiled
                SizedBox(
                  width: 340,
                  child: Text(
                    'Last name',
                    style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                      color: Theme.of(context).hintColor,
                    ),
                  ),
                ),
                const SizedBox(height: 12),
                SizedBox(
                  width: 340,
                  child: TextField(
                    decoration: InputDecoration(
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12),
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 26),
                // email adress textFiled
                SizedBox(
                  width: 340,
                  child: Text(
                    'Email adress',
                    style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                      color: Theme.of(context).hintColor,
                    ),
                  ),
                ),
                const SizedBox(height: 12),
                SizedBox(
                  width: 340,
                  child: TextField(
                    decoration: InputDecoration(
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12),
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 26),
                SizedBox(
                  width: 340,
                  child: Text(
                    'Password',
                    style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                      color: Theme.of(context).hintColor,
                    ),
                  ),
                ),
                const SizedBox(height: 12),
                SizedBox(
                  width: 340,
                  child: TextField(
                    obscureText: _obscureText,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12),
                      ),
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.only(left: 13),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.start,
                    children: [
                      Checkbox(
                        value: !_obscureText,
                        onChanged: (value) {
                          setState(() {
                            _obscureText = !value!;
                          });
                        },
                      ),
                      Text(
                        'Show password',
                        style: Theme.of(context).textTheme.bodyLarge,
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 24),
                // create account button
                GestureDetector(
                  onTap: () {
                    // to gathering more info
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (ctx) => MoreInfoPage()),
                    );
                  },
                  child: Container(
                    height: 56,
                    width: 340,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(30),
                      color: const Color(0xFFE8E8E8),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withAlpha(64),
                          offset: const Offset(0, 4),
                          blurRadius: 4,
                        ),
                      ],
                    ),
                    child: Center(
                      child: Text(
                        'create account',
                        style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                          fontSize: 20,
                          color: Colors.black,
                        ),
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 15),
                GestureDetector(
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => LoginPage()),
                    );
                  },
                  child: Text(
                    'log in instead',
                    style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                      decoration: TextDecoration.underline,
                      color: Colors.black,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

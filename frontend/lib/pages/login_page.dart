import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'package:flutter_trnx_project/pages/sign_up_page.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
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
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  'login',
                  style: Theme.of(context).textTheme.headlineLarge!.copyWith(
                    fontWeight: FontWeight.w500,
                  ),
                ),
                SizedBox(height: 50),
                // email textFiled
                SizedBox(
                  width: 340,
                  child: Text(
                    'Email or mobile phone number',
                    style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                      color: Theme.of(context).hintColor,
                    ),
                  ),
                ),
                SizedBox(height: 12),
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

                SizedBox(height: 26), // spacing between fields

                SizedBox(
                  width: 340,
                  child: Row(
                    children: [
                      // password textFiled
                      Text(
                        'Password',
                        style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                          color: Theme.of(context).hintColor,
                        ),
                      ),
                      Spacer(),
                      IconButton(
                        onPressed: () {
                          setState(() {
                            _obscureText = !_obscureText;
                          });
                        },
                        icon: _obscureText
                            ? Icon(Icons.visibility_off)
                            : Icon(Icons.visibility),
                        color: Theme.of(context).hintColor,
                        iconSize: 20,
                      ),
                      Text(
                        _obscureText ? 'Show' : 'Hide',
                        style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                          color: Theme.of(context).hintColor,
                        ),
                      ),
                    ],
                  ),
                ),
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
                SizedBox(height: 36),
                // login button: add inkwell or gestorD
                GestureDetector(
                  onTap: () {
                    // todo
                  },
                  child: Container(
                    height: 56,
                    width: 340,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(30),
                      color: Color(0xFFE8E8E8),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withAlpha(64), // 25%
                          offset: Offset(0, 4),
                          blurRadius: 4,
                        ),
                      ],
                    ),
                    child: Center(
                      child: Text(
                        'login',
                        style: Theme.of(
                          context,
                        ).textTheme.bodyLarge!.copyWith(fontSize: 20),
                      ),
                    ),
                  ),
                ),
                SizedBox(height: 12),
                // terms of use / privacy policy
                RichText(
                  textAlign: TextAlign.center,
                  text: TextSpan(
                    style: Theme.of(
                      context,
                    ).textTheme.bodyMedium!.copyWith(fontSize: 13),
                    children: [
                      const TextSpan(text: 'By continuing, you agree to the '),
                      TextSpan(
                        text: 'Terms of use',
                        style: const TextStyle(
                          decoration: TextDecoration.underline,
                          fontWeight: FontWeight.w500,
                        ),
                        recognizer: TapGestureRecognizer()
                          ..onTap = () {
                            // todo
                          },
                      ),
                      const TextSpan(text: ' and '),
                      TextSpan(
                        text: 'Privacy Policy.',
                        style: const TextStyle(
                          decoration: TextDecoration.underline,
                          fontWeight: FontWeight.w500,
                        ),
                        recognizer: TapGestureRecognizer()
                          ..onTap = () {
                            // todo
                          },
                      ),
                    ],
                  ),
                ),
                SizedBox(height: 40),
                Row(
                  children: [
                    GestureDetector(
                      onTap: () {
                        // todo
                      },
                      child: Text(
                        'Other issue with login',
                        style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                          decoration: TextDecoration.underline,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ),
                    Spacer(),
                    GestureDetector(
                      onTap: () {
                        // todo
                      },
                      child: Text(
                        'Forget your password',
                        style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                          decoration: TextDecoration.underline,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ),
                  ],
                ),
                SizedBox(height: 40),
                // info
                Row(
                  children: [
                    Expanded(child: Divider(thickness: 2)),
                    Spacer(),

                    Text(
                      "New to our community",
                      style: Theme.of(context).textTheme.titleLarge!.copyWith(
                        color: Theme.of(context).hintColor,
                      ),
                    ),
                    Spacer(),

                    Expanded(child: Divider(thickness: 2)),
                  ],
                ),
                SizedBox(height: 15),
                // create account button
                SizedBox(
                  width: 310,
                  height: 50,
                  child: OutlinedButton(
                    style: ButtonStyle(),
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => SignUpPage()),
                      );
                    },
                    child: Text(
                      'Create an account',
                      style: Theme.of(context).textTheme.titleLarge!.copyWith(
                        color: Theme.of(context).colorScheme.primary,
                      ),
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

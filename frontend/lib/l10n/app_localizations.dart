import 'dart:async';

import 'package:flutter/foundation.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:intl/intl.dart' as intl;

import 'app_localizations_ar.dart';
import 'app_localizations_en.dart';
import 'app_localizations_fr.dart';

// ignore_for_file: type=lint

/// Callers can lookup localized strings with an instance of AppLocalizations
/// returned by `AppLocalizations.of(context)`.
///
/// Applications need to include `AppLocalizations.delegate()` in their app's
/// `localizationDelegates` list, and the locales they support in the app's
/// `supportedLocales` list. For example:
///
/// ```dart
/// import 'l10n/app_localizations.dart';
///
/// return MaterialApp(
///   localizationsDelegates: AppLocalizations.localizationsDelegates,
///   supportedLocales: AppLocalizations.supportedLocales,
///   home: MyApplicationHome(),
/// );
/// ```
///
/// ## Update pubspec.yaml
///
/// Please make sure to update your pubspec.yaml to include the following
/// packages:
///
/// ```yaml
/// dependencies:
///   # Internationalization support.
///   flutter_localizations:
///     sdk: flutter
///   intl: any # Use the pinned version from flutter_localizations
///
///   # Rest of dependencies
/// ```
///
/// ## iOS Applications
///
/// iOS applications define key application metadata, including supported
/// locales, in an Info.plist file that is built into the application bundle.
/// To configure the locales supported by your app, you’ll need to edit this
/// file.
///
/// First, open your project’s ios/Runner.xcworkspace Xcode workspace file.
/// Then, in the Project Navigator, open the Info.plist file under the Runner
/// project’s Runner folder.
///
/// Next, select the Information Property List item, select Add Item from the
/// Editor menu, then select Localizations from the pop-up menu.
///
/// Select and expand the newly-created Localizations item then, for each
/// locale your application supports, add a new item and select the locale
/// you wish to add from the pop-up menu in the Value field. This list should
/// be consistent with the languages listed in the AppLocalizations.supportedLocales
/// property.
abstract class AppLocalizations {
  AppLocalizations(String locale)
    : localeName = intl.Intl.canonicalizedLocale(locale.toString());

  final String localeName;

  static AppLocalizations? of(BuildContext context) {
    return Localizations.of<AppLocalizations>(context, AppLocalizations);
  }

  static const LocalizationsDelegate<AppLocalizations> delegate =
      _AppLocalizationsDelegate();

  /// A list of this localizations delegate along with the default localizations
  /// delegates.
  ///
  /// Returns a list of localizations delegates containing this delegate along with
  /// GlobalMaterialLocalizations.delegate, GlobalCupertinoLocalizations.delegate,
  /// and GlobalWidgetsLocalizations.delegate.
  ///
  /// Additional delegates can be added by appending to this list in
  /// MaterialApp. This list does not have to be used at all if a custom list
  /// of delegates is preferred or required.
  static const List<LocalizationsDelegate<dynamic>> localizationsDelegates =
      <LocalizationsDelegate<dynamic>>[
        delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
      ];

  /// A list of this localizations delegate's supported locales.
  static const List<Locale> supportedLocales = <Locale>[
    Locale('ar'),
    Locale('en'),
    Locale('fr'),
  ];

  /// No description provided for @startJourney.
  ///
  /// In en, this message translates to:
  /// **'Start your journey Now'**
  String get startJourney;

  /// No description provided for @login.
  ///
  /// In en, this message translates to:
  /// **'Login'**
  String get login;

  /// No description provided for @signup.
  ///
  /// In en, this message translates to:
  /// **'Sign Up'**
  String get signup;

  /// No description provided for @continueText.
  ///
  /// In en, this message translates to:
  /// **'Continue'**
  String get continueText;

  /// No description provided for @createAccount.
  ///
  /// In en, this message translates to:
  /// **'create account'**
  String get createAccount;

  /// No description provided for @newToOurCommunity.
  ///
  /// In en, this message translates to:
  /// **'New to our community'**
  String get newToOurCommunity;

  /// No description provided for @emailOrMobile.
  ///
  /// In en, this message translates to:
  /// **'Email or mobile phone number'**
  String get emailOrMobile;

  /// No description provided for @password.
  ///
  /// In en, this message translates to:
  /// **'Password'**
  String get password;

  /// No description provided for @confirmPassword.
  ///
  /// In en, this message translates to:
  /// **'Confirm Password'**
  String get confirmPassword;

  /// No description provided for @firstName.
  ///
  /// In en, this message translates to:
  /// **'First name'**
  String get firstName;

  /// No description provided for @lastName.
  ///
  /// In en, this message translates to:
  /// **'Last name'**
  String get lastName;

  /// No description provided for @emailAddress.
  ///
  /// In en, this message translates to:
  /// **'Email address'**
  String get emailAddress;

  /// No description provided for @showPassword.
  ///
  /// In en, this message translates to:
  /// **'Show password'**
  String get showPassword;

  /// No description provided for @logInInstead.
  ///
  /// In en, this message translates to:
  /// **'log in instead'**
  String get logInInstead;

  /// No description provided for @alreadyHaveAnAccount.
  ///
  /// In en, this message translates to:
  /// **'Already have an account? '**
  String get alreadyHaveAnAccount;

  /// No description provided for @logIn.
  ///
  /// In en, this message translates to:
  /// **'Log in'**
  String get logIn;

  /// No description provided for @otherIssueWithLogin.
  ///
  /// In en, this message translates to:
  /// **'Other issue with login'**
  String get otherIssueWithLogin;

  /// No description provided for @forgotPassword.
  ///
  /// In en, this message translates to:
  /// **'Forget your password?'**
  String get forgotPassword;

  /// No description provided for @byContinuingYouAgreeToThe.
  ///
  /// In en, this message translates to:
  /// **'By continuing, you agree to the '**
  String get byContinuingYouAgreeToThe;

  /// No description provided for @termsOfUse.
  ///
  /// In en, this message translates to:
  /// **'Terms of use'**
  String get termsOfUse;

  /// No description provided for @and.
  ///
  /// In en, this message translates to:
  /// **' and '**
  String get and;

  /// No description provided for @privacyPolicy.
  ///
  /// In en, this message translates to:
  /// **'Privacy Policy'**
  String get privacyPolicy;

  /// No description provided for @hide.
  ///
  /// In en, this message translates to:
  /// **'Hide'**
  String get hide;

  /// No description provided for @show.
  ///
  /// In en, this message translates to:
  /// **'Show'**
  String get show;

  /// No description provided for @tellUsMoreAboutYourself.
  ///
  /// In en, this message translates to:
  /// **'Tell us more about yourself'**
  String get tellUsMoreAboutYourself;

  /// No description provided for @gender.
  ///
  /// In en, this message translates to:
  /// **'Gender'**
  String get gender;

  /// No description provided for @male.
  ///
  /// In en, this message translates to:
  /// **'Male'**
  String get male;

  /// No description provided for @female.
  ///
  /// In en, this message translates to:
  /// **'Female'**
  String get female;

  /// No description provided for @other.
  ///
  /// In en, this message translates to:
  /// **'Other'**
  String get other;

  /// No description provided for @age.
  ///
  /// In en, this message translates to:
  /// **'Age'**
  String get age;

  /// No description provided for @under18.
  ///
  /// In en, this message translates to:
  /// **'Under 18'**
  String get under18;

  /// No description provided for @age18to24.
  ///
  /// In en, this message translates to:
  /// **'18-24'**
  String get age18to24;

  /// No description provided for @age25to34.
  ///
  /// In en, this message translates to:
  /// **'25-34'**
  String get age25to34;

  /// No description provided for @age35to44.
  ///
  /// In en, this message translates to:
  /// **'35-44'**
  String get age35to44;

  /// No description provided for @age45to54.
  ///
  /// In en, this message translates to:
  /// **'45-54'**
  String get age45to54;

  /// No description provided for @age55to64.
  ///
  /// In en, this message translates to:
  /// **'55-64'**
  String get age55to64;

  /// No description provided for @age65plus.
  ///
  /// In en, this message translates to:
  /// **'65+'**
  String get age65plus;

  /// No description provided for @weight.
  ///
  /// In en, this message translates to:
  /// **'Weight'**
  String get weight;

  /// No description provided for @height.
  ///
  /// In en, this message translates to:
  /// **'Height'**
  String get height;

  /// No description provided for @goodMorning.
  ///
  /// In en, this message translates to:
  /// **'Good Morning'**
  String get goodMorning;

  /// No description provided for @goodAfternoon.
  ///
  /// In en, this message translates to:
  /// **'Good Afternoon'**
  String get goodAfternoon;

  /// No description provided for @goodEvening.
  ///
  /// In en, this message translates to:
  /// **'Good Evening'**
  String get goodEvening;

  /// No description provided for @stepsWalked.
  ///
  /// In en, this message translates to:
  /// **'Steps Walked'**
  String get stepsWalked;

  /// No description provided for @steps.
  ///
  /// In en, this message translates to:
  /// **'Steps'**
  String get steps;

  /// No description provided for @km.
  ///
  /// In en, this message translates to:
  /// **'km'**
  String get km;

  /// No description provided for @kcal.
  ///
  /// In en, this message translates to:
  /// **'kcal'**
  String get kcal;

  /// No description provided for @caloriesBurned.
  ///
  /// In en, this message translates to:
  /// **'Calories Burned'**
  String get caloriesBurned;

  /// No description provided for @updateGoal.
  ///
  /// In en, this message translates to:
  /// **'Update Goal'**
  String get updateGoal;

  /// No description provided for @waterIntake.
  ///
  /// In en, this message translates to:
  /// **'Water Intake'**
  String get waterIntake;

  /// No description provided for @ml.
  ///
  /// In en, this message translates to:
  /// **'ml'**
  String get ml;

  /// No description provided for @cup.
  ///
  /// In en, this message translates to:
  /// **'cup'**
  String get cup;

  /// No description provided for @aiAssistant.
  ///
  /// In en, this message translates to:
  /// **'AI Assistant'**
  String get aiAssistant;

  /// No description provided for @howCanIHelpYouToday.
  ///
  /// In en, this message translates to:
  /// **'How can I help you today'**
  String get howCanIHelpYouToday;

  /// No description provided for @foodIdeas.
  ///
  /// In en, this message translates to:
  /// **'Food ideas'**
  String get foodIdeas;

  /// No description provided for @howToReduce.
  ///
  /// In en, this message translates to:
  /// **'how to reduc...'**
  String get howToReduce;

  /// No description provided for @workoutRoutines.
  ///
  /// In en, this message translates to:
  /// **'Workout routines'**
  String get workoutRoutines;

  /// No description provided for @whatsOnYourMind.
  ///
  /// In en, this message translates to:
  /// **'What\'s on your mind'**
  String get whatsOnYourMind;

  /// No description provided for @weightLossJourney.
  ///
  /// In en, this message translates to:
  /// **'weight loss journey'**
  String get weightLossJourney;

  /// No description provided for @lastMonth.
  ///
  /// In en, this message translates to:
  /// **'Last Month'**
  String get lastMonth;

  /// No description provided for @currentMonth.
  ///
  /// In en, this message translates to:
  /// **'Current Month'**
  String get currentMonth;

  /// No description provided for @profile.
  ///
  /// In en, this message translates to:
  /// **'Profile'**
  String get profile;

  /// No description provided for @changePersonalInfo.
  ///
  /// In en, this message translates to:
  /// **'Change personnal infos'**
  String get changePersonalInfo;

  /// No description provided for @memberSince.
  ///
  /// In en, this message translates to:
  /// **'Membre depuis'**
  String get memberSince;

  /// No description provided for @daysStreak.
  ///
  /// In en, this message translates to:
  /// **'Days Streak'**
  String get daysStreak;

  /// No description provided for @weightLost.
  ///
  /// In en, this message translates to:
  /// **'Weight lost'**
  String get weightLost;

  /// No description provided for @actualWeight.
  ///
  /// In en, this message translates to:
  /// **'Actual weight'**
  String get actualWeight;

  /// No description provided for @goal.
  ///
  /// In en, this message translates to:
  /// **'Goal'**
  String get goal;

  /// No description provided for @progressToGoal.
  ///
  /// In en, this message translates to:
  /// **'Plus que 2kg à perdre • Objectif: septembre 2025'**
  String get progressToGoal;

  /// No description provided for @aidSupport.
  ///
  /// In en, this message translates to:
  /// **'Aide & Support'**
  String get aidSupport;

  /// No description provided for @helpCenter.
  ///
  /// In en, this message translates to:
  /// **'Centre d\'aide FAQ et tutoriels'**
  String get helpCenter;

  /// No description provided for @contactSupport.
  ///
  /// In en, this message translates to:
  /// **'Contacter le Support'**
  String get contactSupport;

  /// No description provided for @legal.
  ///
  /// In en, this message translates to:
  /// **'Légal'**
  String get legal;

  /// No description provided for @conditionsOfUse.
  ///
  /// In en, this message translates to:
  /// **'Conditions d\'utilisation'**
  String get conditionsOfUse;

  /// No description provided for @cancelMembership.
  ///
  /// In en, this message translates to:
  /// **'Cancel My Membership'**
  String get cancelMembership;

  /// No description provided for @privacyPolicyTitle.
  ///
  /// In en, this message translates to:
  /// **'Politique de confidentialité'**
  String get privacyPolicyTitle;

  /// No description provided for @name.
  ///
  /// In en, this message translates to:
  /// **'Name'**
  String get name;
}

class _AppLocalizationsDelegate
    extends LocalizationsDelegate<AppLocalizations> {
  const _AppLocalizationsDelegate();

  @override
  Future<AppLocalizations> load(Locale locale) {
    return SynchronousFuture<AppLocalizations>(lookupAppLocalizations(locale));
  }

  @override
  bool isSupported(Locale locale) =>
      <String>['ar', 'en', 'fr'].contains(locale.languageCode);

  @override
  bool shouldReload(_AppLocalizationsDelegate old) => false;
}

AppLocalizations lookupAppLocalizations(Locale locale) {
  // Lookup logic when only language code is specified.
  switch (locale.languageCode) {
    case 'ar':
      return AppLocalizationsAr();
    case 'en':
      return AppLocalizationsEn();
    case 'fr':
      return AppLocalizationsFr();
  }

  throw FlutterError(
    'AppLocalizations.delegate failed to load unsupported locale "$locale". This is likely '
    'an issue with the localizations generation tool. Please file an issue '
    'on GitHub with a reproducible sample app and the gen-l10n configuration '
    'that was used.',
  );
}

part of index;

class UserProfile {
  final String name;
  final String email;
  final String? profileImagePath;
  final DateTime memberSince;
  final int streak;
  final double weightLost;
  final double actualWeight;
  final double goalWeight;
  final DateTime? goalDate;

  UserProfile({
    required this.name,
    required this.email,
    this.profileImagePath,
    required this.memberSince,
    this.streak = 0,
    this.weightLost = 0.0,
    required this.actualWeight,
    required this.goalWeight,
    this.goalDate,
  });

  UserProfile copyWith({
    String? name,
    String? email,
    String? profileImagePath,
    DateTime? memberSince,
    int? streak,
    double? weightLost,
    double? actualWeight,
    double? goalWeight,
    DateTime? goalDate,
  }) {
    return UserProfile(
      name: name ?? this.name,
      email: email ?? this.email,
      profileImagePath: profileImagePath ?? this.profileImagePath,
      memberSince: memberSince ?? this.memberSince,
      streak: streak ?? this.streak,
      weightLost: weightLost ?? this.weightLost,
      actualWeight: actualWeight ?? this.actualWeight,
      goalWeight: goalWeight ?? this.goalWeight,
      goalDate: goalDate ?? this.goalDate,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'name': name,
      'email': email,
      'profileImagePath': profileImagePath,
      'memberSince': memberSince.toIso8601String(),
      'streak': streak,
      'weightLost': weightLost,
      'actualWeight': actualWeight,
      'goalWeight': goalWeight,
      'goalDate': goalDate?.toIso8601String(),
    };
  }

  factory UserProfile.fromJson(Map<String, dynamic> json) {
    return UserProfile(
      name: json['name'] as String,
      email: json['email'] as String,
      profileImagePath: json['profileImagePath'] as String?,
      memberSince: DateTime.parse(json['memberSince'] as String),
      streak: json['streak'] as int? ?? 0,
      weightLost: (json['weightLost'] as num?)?.toDouble() ?? 0.0,
      actualWeight: (json['actualWeight'] as num).toDouble(),
      goalWeight: (json['goalWeight'] as num).toDouble(),
      goalDate: json['goalDate'] != null 
          ? DateTime.parse(json['goalDate'] as String) 
          : null,
    );
  }
}

class AuthProvider extends ChangeNotifier {
  UserProfile? _userProfile;
  final StockState _stock = StockState();

  UserProfile? get userProfile => _userProfile;

  AuthProvider() {
    _loadUserProfile();
  }

  Future<void> _loadUserProfile() async {
    await _stock.loadStock();
    final profileJson = _stock.get<String>(EntetyStock.userProfile);
    if (profileJson != null) {
      try {
        _userProfile = UserProfile.fromJson(jsonDecode(profileJson));
        notifyListeners();
      } catch (e) {
        _initializeDefaultProfile();
      }
    } else {
      _initializeDefaultProfile();
    }
  }

  void _initializeDefaultProfile() {
    _userProfile = UserProfile(
      name: 'Mark Philips',
      email: 'mark.philips@example.com',
      memberSince: DateTime(2025, 8, 1),
      streak: 10,
      weightLost: 2.5,
      actualWeight: 86.0,
      goalWeight: 75.0,
      goalDate: DateTime(2025, 9, 1),
    );
    _saveUserProfile();
  }

  Future<void> _saveUserProfile() async {
    if (_userProfile != null) {
      await _stock.set(
        EntetyStock.userProfile,
        jsonEncode(_userProfile!.toJson()),
      );
    }
  }

  Future<void> updateProfile({
    String? name,
    String? email,
    double? actualWeight,
    double? goalWeight,
    DateTime? goalDate,
  }) async {
    if (_userProfile == null) return;

    _userProfile = _userProfile!.copyWith(
      name: name,
      email: email,
      actualWeight: actualWeight,
      goalWeight: goalWeight,
      goalDate: goalDate,
    );

    await _saveUserProfile();
    notifyListeners();
  }

  Future<void> updateProfileImage(String imagePath) async {
    if (_userProfile == null) return;

    _userProfile = _userProfile!.copyWith(profileImagePath: imagePath);
    await _saveUserProfile();
    notifyListeners();
  }

  double getProgressPercentage() {
    if (_userProfile == null) return 0.0;
    
    final initialWeight = _userProfile!.actualWeight + _userProfile!.weightLost;
    final targetWeight = _userProfile!.goalWeight;
    final currentWeight = _userProfile!.actualWeight;
    
    if (initialWeight == targetWeight) return 100.0;
    
    final totalWeightToLose = initialWeight - targetWeight;
    final weightLostSoFar = initialWeight - currentWeight;
    
    return ((weightLostSoFar / totalWeightToLose) * 100).clamp(0.0, 100.0);
  }

  int getDaysSinceMember() {
    if (_userProfile == null) return 0;
    return DateTime.now().difference(_userProfile!.memberSince).inDays;
  }
}

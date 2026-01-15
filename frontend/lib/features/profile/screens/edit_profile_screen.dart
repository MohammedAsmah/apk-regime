part of 'index.dart';

class EditProfileScreen extends StatefulWidget {
  const EditProfileScreen({super.key});

  @override
  State<EditProfileScreen> createState() => _EditProfileScreenState();
}

class _EditProfileScreenState extends State<EditProfileScreen> {
  final TextEditingController _nameController = TextEditingController();
  final ImagePicker _picker = ImagePicker();
  String? _tempImagePath;

  @override
  void initState() {
    super.initState();
    final authProvider = context.read<AuthProvider>();
    final userProfile = authProvider.userProfile;
    if (userProfile != null) {
      _nameController.text = userProfile.name;
      _tempImagePath = userProfile.profileImagePath;
    }
  }

  @override
  void dispose() {
    _nameController.dispose();
    super.dispose();
  }

  Future<void> _pickImage() async {
    showModalBottomSheet(
      context: context,
      backgroundColor: AppColors.black,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(
          top: Radius.circular(AppDimensions.radiusL),
        ),
      ),
      builder: (context) => SafeArea(
        child: Padding(
          padding: EdgeInsets.all(AppDimensions.l),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              ListTile(
                leading: Icon(Icons.camera_alt, color: AppColors.white),
                title: Text(
                  'Take Photo',
                  style: TextStyle(color: AppColors.white),
                ),
                onTap: () async {
                  Navigator.pop(context);
                  final XFile? image = await _picker.pickImage(
                    source: ImageSource.camera,
                    maxWidth: 1024,
                    maxHeight: 1024,
                    imageQuality: 85,
                  );
                  if (image != null) {
                    setState(() {
                      _tempImagePath = image.path;
                    });
                  }
                },
              ),
              ListTile(
                leading: Icon(Icons.photo_library, color: AppColors.white),
                title: Text(
                  'Choose from Gallery',
                  style: TextStyle(color: AppColors.white),
                ),
                onTap: () async {
                  Navigator.pop(context);
                  final XFile? image = await _picker.pickImage(
                    source: ImageSource.gallery,
                    maxWidth: 1024,
                    maxHeight: 1024,
                    imageQuality: 85,
                  );
                  if (image != null) {
                    setState(() {
                      _tempImagePath = image.path;
                    });
                  }
                },
              ),
            ],
          ),
        ),
      ),
    );
  }

  Future<void> _saveProfile() async {
    final authProvider = context.read<AuthProvider>();
    
    if (_nameController.text.isNotEmpty) {
      await authProvider.updateProfile(name: _nameController.text);
    }
    
    if (_tempImagePath != null && 
        _tempImagePath != authProvider.userProfile?.profileImagePath) {
      await authProvider.updateProfileImage(_tempImagePath!);
    }
    
    if (mounted) {
      context.pop();
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final l10n = AppLocalizations.of(context)!;

    return Scaffold(
      backgroundColor: AppColors.black,
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.symmetric(
            horizontal: AppDimensions.screenPaddingHorizontal,
            vertical: AppDimensions.l,
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  IconButton(
                    onPressed: () => context.pop(),
                    icon: Icon(
                      Icons.close,
                      color: AppColors.white,
                      size: 28.sp,
                    ),
                  ),
                  TextButton(
                    onPressed: _saveProfile,
                    child: Text(
                      'Save',
                      style: TextStyle(
                        color: AppColors.successGreen,
                        fontSize: 16.sp,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),
                ],
              ),
              SizedBox(height: AppDimensions.l),
              Center(
                child: Text(
                  l10n.changePersonalInfo,
                  style: theme.textTheme.headlineLarge?.copyWith(
                    color: AppColors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 24.sp,
                  ),
                ),
              ),
              SizedBox(height: AppDimensions.xl),
              Center(
                child: Stack(
                  children: [
                    GestureDetector(
                      onTap: _pickImage,
                      child: Container(
                        width: 150.w,
                        height: 150.w,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          color: AppColors.white.withValues(alpha: 0.1),
                          image: _tempImagePath != null
                              ? DecorationImage(
                                  image: FileImage(File(_tempImagePath!)),
                                  fit: BoxFit.cover,
                                )
                              : null,
                        ),
                        child: _tempImagePath == null
                            ? Icon(
                                Icons.person,
                                size: 80.sp,
                                color: AppColors.white.withValues(alpha: 0.5),
                              )
                            : null,
                      ),
                    ),
                    Positioned(
                      bottom: 0,
                      right: 0,
                      child: GestureDetector(
                        onTap: _pickImage,
                        child: Container(
                          width: 48.w,
                          height: 48.w,
                          decoration: BoxDecoration(
                            color: AppColors.black,
                            shape: BoxShape.circle,
                            border: Border.all(
                              color: AppColors.white.withValues(alpha: 0.3),
                              width: 2,
                            ),
                          ),
                          child: Icon(
                            Icons.edit,
                            size: 24.sp,
                            color: AppColors.white,
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              SizedBox(height: AppDimensions.xxl),
              Text(
                'Contacter le Support',
                style: theme.textTheme.bodyMedium?.copyWith(
                  color: AppColors.white.withValues(alpha: 0.5),
                  fontSize: 12.sp,
                ),
              ),
              SizedBox(height: AppDimensions.l),
              Container(
                padding: EdgeInsets.symmetric(
                  horizontal: AppDimensions.m,
                  vertical: AppDimensions.s,
                ),
                decoration: BoxDecoration(
                  color: AppColors.white.withValues(alpha: 0.05),
                  borderRadius: BorderRadius.circular(AppDimensions.radiusM),
                  border: Border.all(
                    color: AppColors.white.withValues(alpha: 0.1),
                    width: 1,
                  ),
                ),
                child: Row(
                  children: [
                    Text(
                      l10n.name,
                      style: theme.textTheme.bodyLarge?.copyWith(
                        color: AppColors.white,
                        fontSize: 16.sp,
                      ),
                    ),
                    SizedBox(width: AppDimensions.m),
                    Expanded(
                      child: TextField(
                        controller: _nameController,
                        style: TextStyle(
                          color: AppColors.white,
                          fontSize: 16.sp,
                        ),
                        decoration: InputDecoration(
                          border: InputBorder.none,
                          hintText: 'Enter your name',
                          hintStyle: TextStyle(
                            color: AppColors.white.withValues(alpha: 0.3),
                          ),
                          isDense: true,
                          contentPadding: EdgeInsets.zero,
                        ),
                      ),
                    ),
                    Icon(
                      Icons.edit,
                      color: AppColors.white.withValues(alpha: 0.5),
                      size: 20.sp,
                    ),
                  ],
                ),
              ),
               SizedBox(height: AppDimensions.xl,),
            ],
          ),
        ),
      ),
    );
  }
}

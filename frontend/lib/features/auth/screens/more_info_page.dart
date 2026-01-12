part of index;

class MoreInfoPage extends StatefulWidget {
  const MoreInfoPage({super.key});

  @override
  State<MoreInfoPage> createState() => _MoreInfoPageState();
}

class _MoreInfoPageState extends State<MoreInfoPage> {
  late List<bool> _selectedGender;
  late List<bool> _selectedAgeRange;
  late TextEditingController _weightController;
  late TextEditingController _heightController;
  String _weightUnit = 'kg';
  String _heightUnit = 'cm';

  List<String> _getAgeRanges(AppLocalizations l10n) {
    return [
      l10n.under18,
      l10n.age18to24,
      l10n.age25to34,
      l10n.age35to44,
      l10n.age45to54,
      l10n.age55to64,
      l10n.age65plus,
    ];
  }

  @override
  void initState() {
    super.initState();
    _selectedGender = [true, false, false];
    _selectedAgeRange = List<bool>.filled(7, false);
    _weightController = TextEditingController();
    _heightController = TextEditingController();
  }

  @override
  void dispose() {
    _weightController.dispose();
    _heightController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    var l10n = AppLocalizations.of(context)!;
    final ageRanges = _getAgeRanges(l10n);
    
    return Scaffold(
      backgroundColor: ColorScheme.of(context).background,
      body: SafeArea(
        child: Container(
          padding: EdgeInsets.symmetric(
            horizontal: AppDimensions.screenPaddingHorizontal,
            vertical: AppDimensions.screenPaddingVertical,
          ),
          child: SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Text(
                  l10n.tellUsMoreAboutYourself,
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.headlineLarge!.copyWith(
                    fontWeight: FontWeight.w500,
                    fontFamily: 'Poppins',
                  ),
                ),
                SizedBox(height: 50.h),
                SizedBox(
                  width: 340.w,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        l10n.gender,
                        style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                          color: Theme.of(context).hintColor,
                        ),
                      ),
                      SizedBox(height: 12.h),
                      ToggleButtons(
                        direction: Axis.horizontal,
                        onPressed: (int index) {
                          setState(() {
                            for (int i = 0; i < _selectedGender.length; i++) {
                              _selectedGender[i] = i == index;
                            }
                          });
                        },
                        borderRadius: BorderRadius.all(
                          Radius.circular(AppDimensions.radiusS),
                        ),
                        selectedBorderColor: Theme.of(context).colorScheme.outline,
                        fillColor: Theme.of(context).colorScheme.inversePrimary,
                        constraints: BoxConstraints(
                          minHeight: AppDimensions.buttonHeight,
                          minWidth: 100.w,
                        ),
                        isSelected: _selectedGender,
                        children: [
                          Text(
                            l10n.male,
                            style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          Text(
                            l10n.female,
                            style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          Text(
                            l10n.other,
                            style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),

                SizedBox(height: AppDimensions.xl),
                SizedBox(
                  width: 340.w,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        l10n.age,
                        style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                          color: Theme.of(context).hintColor,
                        ),
                      ),
                      SizedBox(height: 12.h),
                      Wrap(
                        spacing: 8.w,
                        runSpacing: 8.h,
                        children: List<Widget>.generate(ageRanges.length, (
                          int index,
                        ) {
                          return GestureDetector(
                            onTap: () {
                              setState(() {
                                for (int i = 0; i < _selectedAgeRange.length; i++) {
                                  _selectedAgeRange[i] = i == index;
                                }
                              });
                            },
                            child: Container(
                              padding: EdgeInsets.symmetric(
                                horizontal: AppDimensions.m,
                                vertical: AppDimensions.s,
                              ),
                              decoration: BoxDecoration(
                                borderRadius: BorderRadius.circular(AppDimensions.radiusS),
                                border: Border.all(
                                  color: _selectedAgeRange[index]
                                      ? Theme.of(context).colorScheme.outline
                                      : Theme.of(context).colorScheme.outlineVariant,
                                  width: 2,
                                ),
                                color: _selectedAgeRange[index]
                                    ? Theme.of(context).colorScheme.inversePrimary
                                    : Colors.transparent,
                              ),
                              child: Text(
                                ageRanges[index],
                                style: Theme.of(context).textTheme.bodyMedium!
                                    .copyWith(fontWeight: FontWeight.w600),
                              ),
                            ),
                          );
                        }),
                      ),
                    ],
                  ),
                ),

                SizedBox(height: AppDimensions.xl),
                SizedBox(
                  width: 340.w,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        l10n.weight,
                        style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                          color: Theme.of(context).hintColor,
                        ),
                      ),
                      SizedBox(height: 12.h),
                      Row(
                        children: [
                          Expanded(
                            child: TextField(
                              controller: _weightController,
                              keyboardType: const TextInputType.numberWithOptions(
                                decimal: true,
                              ),
                              decoration: InputDecoration(
                                hintText: _weightUnit == 'kg' ? '0.0 kg' : '0.0 lb',
                              ),
                            ),
                          ),
                          SizedBox(width: AppDimensions.s),
                          SizedBox(
                            width: 100.w,
                            child: DropdownButtonFormField<String>(
                              value: _weightUnit,
                              items: const [
                                DropdownMenuItem(value: 'kg', child: Text('kg')),
                                DropdownMenuItem(value: 'lb', child: Text('lb')),
                              ],
                              onChanged: (value) {
                                setState(() {
                                  _weightUnit = value ?? 'kg';
                                });
                              },
                              decoration: const InputDecoration(
                                contentPadding: EdgeInsets.symmetric(horizontal: 12),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),

                SizedBox(height: AppDimensions.xs),
                SizedBox(
                  width: 340.w,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        l10n.height,
                        style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                          color: Theme.of(context).hintColor,
                        ),
                      ),
                      SizedBox(height: 12.h),
                      Row(
                        children: [
                          Expanded(
                            child: TextField(
                              controller: _heightController,
                              keyboardType: const TextInputType.numberWithOptions(
                                decimal: true,
                              ),
                              decoration: InputDecoration(
                                hintText: _heightUnit == 'cm' ? '0.0 cm' : '0.0 ft',
                              ),
                            ),
                          ),
                          SizedBox(width: AppDimensions.s),
                          SizedBox(
                            width: 100.w,
                            child: DropdownButtonFormField<String>(
                              value: _heightUnit,
                              items: const [
                                DropdownMenuItem(value: 'cm', child: Text('cm')),
                                DropdownMenuItem(value: 'ft', child: Text('ft')),
                              ],
                              onChanged: (value) {
                                setState(() {
                                  _heightUnit = value ?? 'cm';
                                });
                              },
                              decoration: const InputDecoration(
                                contentPadding: EdgeInsets.symmetric(horizontal: 12),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),

                SizedBox(height: AppDimensions.xl),

                OutlinedButton(
                  onPressed: () {
                    context.pushReplacement('/home');
                  },
                  child: Text(l10n.continueText, style: TextStyle(fontSize: 20.sp)),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

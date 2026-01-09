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

  final List<String> _ageRanges = [
    'Under 18',
    '18-24',
    '25-34',
    '35-44',
    '45-54',
    '55-64',
    '65+',
  ];

  @override
  void initState() {
    super.initState();
    _selectedGender = [true, false, false]; // Male selected by default
    _selectedAgeRange = List<bool>.filled(_ageRanges.length, false);
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
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 40, horizontal: 31),
          child: SingleChildScrollView(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  textAlign: TextAlign.center,
                  'Tell us more about yourself',
                  style: Theme.of(context).textTheme.headlineLarge!.copyWith(
                    fontWeight: FontWeight.w500,
                  ),
                ),
                const SizedBox(height: 40),
                // Gender Section
                Text(
                  'Gender',
                  style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                    color: Theme.of(context).hintColor,
                  ),
                ),
                const SizedBox(height: 12),
                ToggleButtons(
                  direction: Axis.horizontal,
                  onPressed: (int index) {
                    setState(() {
                      for (int i = 0; i < _selectedGender.length; i++) {
                        _selectedGender[i] = i == index;
                      }
                    });
                  },
                  borderRadius: const BorderRadius.all(Radius.circular(12)),
                  selectedBorderColor: Theme.of(context).colorScheme.outline,
                  fillColor: Theme.of(context).colorScheme.inversePrimary,
                  constraints: const BoxConstraints(
                    minHeight: 50.0,
                    minWidth: 100.0,
                  ),
                  isSelected: _selectedGender,
                  children: [
                    Text(
                      'Male',
                      style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    Text(
                      'Female',
                      style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    Text(
                      'Other',
                      style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 40),
                // Age Range Section
                Text(
                  'Age',
                  style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                    color: Theme.of(context).hintColor,
                  ),
                ),
                const SizedBox(height: 12),
                Wrap(
                  spacing: 8,
                  runSpacing: 8,
                  children: List<Widget>.generate(_ageRanges.length, (
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
                        padding: const EdgeInsets.symmetric(
                          horizontal: 16,
                          vertical: 12,
                        ),
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(12),
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
                          _ageRanges[index],
                          style: Theme.of(context).textTheme.bodyMedium!
                              .copyWith(fontWeight: FontWeight.w600),
                        ),
                      ),
                    );
                  }),
                ),
                const SizedBox(height: 40),
                // Weight Section
                Text(
                  'Weight',
                  style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                    color: Theme.of(context).hintColor,
                  ),
                ),
                const SizedBox(height: 12),
                Row(
                  children: [
                    Expanded(
                      child: TextField(
                        controller: _weightController,
                        keyboardType: const TextInputType.numberWithOptions(
                          decimal: true,
                        ),
                        decoration: InputDecoration(
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(12),
                          ),
                          hintText: _weightUnit == 'kg' ? '0.0 kg' : '0.0 lb',
                          contentPadding: const EdgeInsets.symmetric(
                            horizontal: 16,
                            vertical: 12,
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(width: 12),
                    SizedBox(
                      width: 100,
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
                        decoration: InputDecoration(
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(12),
                          ),
                          contentPadding: const EdgeInsets.symmetric(
                            horizontal: 16,
                            vertical: 12,
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 26),
                // Height Section
                Text(
                  'Height',
                  style: Theme.of(context).textTheme.bodyLarge!.copyWith(
                    color: Theme.of(context).hintColor,
                  ),
                ),
                const SizedBox(height: 12),
                Row(
                  children: [
                    Expanded(
                      child: TextField(
                        controller: _heightController,
                        keyboardType: const TextInputType.numberWithOptions(
                          decimal: true,
                        ),
                        decoration: InputDecoration(
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(12),
                          ),
                          hintText: _heightUnit == 'cm' ? '0.0 cm' : '0.0 ft',
                          contentPadding: const EdgeInsets.symmetric(
                            horizontal: 16,
                            vertical: 12,
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(width: 12),
                    SizedBox(
                      width: 100,
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
                        decoration: InputDecoration(
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(12),
                          ),
                          contentPadding: const EdgeInsets.symmetric(
                            horizontal: 16,
                            vertical: 12,
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
                SizedBox(height: 40),
                // Continue button
                Align(
                  alignment: Alignment.center,
                  child: GestureDetector(
                    onTap: () {
                      // to HOME
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (ctx) => Placeholder()),
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
                          'Continue',
                          style: Theme.of(context).textTheme.bodyLarge!
                              .copyWith(fontSize: 20, color: Colors.black),
                        ),
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

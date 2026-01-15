part of 'index.dart';

class CoachScreen extends StatefulWidget {
  const CoachScreen({super.key});

  @override
  State<CoachScreen> createState() => _CoachScreenState();
}

class _CoachScreenState extends State<CoachScreen> {
  final TextEditingController _inputController = TextEditingController();
  final ScrollController _scrollController = ScrollController();
  final List<ChatMessage> _messages = [];

  @override
  void initState() {
    super.initState();
    _initializeChat();
  }

  @override
  void dispose() {
    _inputController.dispose();
    _scrollController.dispose();
    super.dispose();
  }

  void _initializeChat() {
    _messages.addAll([
      ChatMessage(
        text: 'Introduce yourself for me please',
        sender: MessageSender.user,
      ),
      ChatMessage(
        text: 'Absolutely 💪 I\'m in — your personal AI sport coach at your service.\nBefore we start, coach mode needs to know a few things:',
        sender: MessageSender.ai,
        bulletPoints: [
          'What\'s your current fitness goal? (e.g. build muscle, lose fat, get more flexible, improve endurance...)',
          'Do you want me to act more like a strict coach who pushes you hard, or a chill motivator who keeps it supportive and fun?',
          'Any equipment or space you have access to (gym, home, dumbbells, just bodyweight, etc.)?',
        ],
      ),
      ChatMessage(
        text: 'I want to lose weight',
        sender: MessageSender.user,
      ),
      ChatMessage(
        text: 'Perfect — goal locked in 🔥 weight loss mode activated.\nBefore I build your plan, I need just a few more things so I can coach you properly:',
        sender: MessageSender.ai,
        bulletPoints: [
          '⚖️ Do you know your current weight (roughly) and your target weight?',
          '🏋️ Do you prefer home workouts or the gym?',
          '⏰ How many days per week are you ready to train?',
          '🥗 Do you want me to include light nutrition guidance (like habits and tips) or focus only on workouts?',
        ],
      ),
    ]);
  }

  void _handleQuickReply(String reply) {
    _sendMessage(reply);
  }

  void _sendMessage(String text) {
    if (text.trim().isEmpty) return;

    setState(() {
      _messages.add(ChatMessage(
        text: text,
        sender: MessageSender.user,
      ));
    });

    _inputController.clear();
    _scrollToBottom();

    Future.delayed(const Duration(milliseconds: 500), () {
      setState(() {
        _messages.add(ChatMessage(
          text: 'Got it! Thanks for sharing. Let me process that and create your personalized plan...',
          sender: MessageSender.ai,
        ));
      });
      _scrollToBottom();
    });
  }

  void _scrollToBottom() {
    Future.delayed(const Duration(milliseconds: 100), () {
      if (_scrollController.hasClients) {
        _scrollController.animateTo(
          _scrollController.position.maxScrollExtent,
          duration: const Duration(milliseconds: 300),
          curve: Curves.easeOut,
        );
      }
    });
  }

 
  void _handleSubmit() {
    _sendMessage(_inputController.text);
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;
    final l10n = AppLocalizations.of(context)!;

    return Scaffold(
      backgroundColor: isDark ? AppColors.darkBackground : AppColors.lightBackground,
      body: SafeArea(
        child: Column(
          children: [
            Expanded(
              child: ListView.builder(
                controller: _scrollController,
                padding: EdgeInsets.symmetric(vertical: AppDimensions.m),
                itemCount: _messages.length,
                itemBuilder: (context, index) {
                  return ChatBubble(
                    message: _messages[index],
                    onQuickReplyTap: _handleQuickReply,
                  );
                },
              ),
            ),
            Container(
              padding: EdgeInsets.all(AppDimensions.m),
              decoration: BoxDecoration(
                color: isDark ? AppColors.darkBackground : AppColors.lightBackground,
                border: Border(
                  top: BorderSide(
                    color: isDark ? AppColors.darkBorder : AppColors.lightBorder,
                    width: 1,
                  ),
                ),
              ),
              child: Row(
                children: [
                  Container(
                    padding: EdgeInsets.symmetric(
                      horizontal: AppDimensions.s,
                      vertical: AppDimensions.xs,
                    ),
                    decoration: BoxDecoration(
                      color: isDark
                          ? AppColors.darkSurface
                          : AppColors.lightSurface,
                      borderRadius: BorderRadius.circular(AppDimensions.radiusFull),
                    ),
                    child: Row(
                      children: [
                        Icon(
                          Icons.language,
                          size: 16.sp,
                          color: isDark
                              ? AppColors.darkTextSecondary
                              : AppColors.lightTextSecondary,
                        ),
                        SizedBox(width: AppDimensions.xxs),
                        Text(
                          'Français',
                          style: theme.textTheme.bodySmall?.copyWith(
                            color: isDark
                                ? AppColors.darkTextSecondary
                                : AppColors.lightTextSecondary,
                            fontSize: 12.sp,
                          ),
                        ),
                        SizedBox(width: AppDimensions.xxs),
                        Icon(
                          Icons.arrow_drop_down,
                          size: 16.sp,
                          color: isDark
                              ? AppColors.darkTextSecondary
                              : AppColors.lightTextSecondary,
                        ),
                      ],
                    ),
                  ),
                  SizedBox(width: AppDimensions.s),
                  Expanded(
                    child: Container(
                      decoration: BoxDecoration(
                        color: isDark
                            ? AppColors.darkSurface
                            : AppColors.lightSurface,
                        borderRadius: BorderRadius.circular(AppDimensions.radiusFull),
                      ),
                      child: TextField(
                        controller: _inputController,
                        style: TextStyle(
                          color: isDark
                              ? AppColors.darkTextPrimary
                              : AppColors.lightTextPrimary,
                          fontSize: 14.sp,
                        ),
                        decoration: InputDecoration(
                          hintText: l10n.whatsOnYourMind,
                          hintStyle: TextStyle(
                            color: isDark
                                ? AppColors.darkTextTertiary
                                : AppColors.lightTextTertiary,
                            fontSize: 14.sp,
                          ),
                          border: InputBorder.none,
                          contentPadding: EdgeInsets.symmetric(
                            horizontal: AppDimensions.m,
                            vertical: AppDimensions.s,
                          ),
                          suffixIcon: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              IconButton(
                                onPressed: () {},
                                icon: Icon(
                                  Icons.add_circle_outline,
                                  color: isDark
                                      ? AppColors.darkTextSecondary
                                      : AppColors.lightTextSecondary,
                                  size: 20.sp,
                                ),
                              ),
                              IconButton(
                                onPressed: () {},
                                icon: Icon(
                                  Icons.add_photo_alternate_outlined,
                                  color: isDark
                                      ? AppColors.darkTextSecondary
                                      : AppColors.lightTextSecondary,
                                  size: 20.sp,
                                ),
                              ),
                              IconButton(
                                onPressed: () {},
                                icon: Icon(
                                  Icons.mic_none,
                                  color: isDark
                                      ? AppColors.darkTextSecondary
                                      : AppColors.lightTextSecondary,
                                  size: 20.sp,
                                ),
                              ),
                            ],
                          ),
                        ),
                        onSubmitted: (_) => _handleSubmit(),
                      ),
                    ),
                  ),
                  SizedBox(width: AppDimensions.s),
                  GestureDetector(
                    onTap: _handleSubmit,
                    child: Container(
                      width: 40.w,
                      height: 40.h,
                      decoration: BoxDecoration(
                        color: AppColors.black,
                        shape: BoxShape.circle,
                      ),
                      child: Icon(
                        Icons.arrow_upward,
                        color: AppColors.white,
                        size: 20.sp,
                      ),
                    ),
                  ),
                  SizedBox(height: AppDimensions.xl,),
                  SizedBox(height: AppDimensions.xxl,)
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

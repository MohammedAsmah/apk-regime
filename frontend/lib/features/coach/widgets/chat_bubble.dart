part of 'index.dart';

enum MessageSender { user, ai }

class ChatMessage {
  final String text;
  final MessageSender sender;
  final List<String>? bulletPoints;
  final List<String>? quickReplies;

  ChatMessage({
    required this.text,
    required this.sender,
    this.bulletPoints,
    this.quickReplies,
  });
}

class ChatBubble extends StatelessWidget {
  final ChatMessage message;
  final Function(String)? onQuickReplyTap;

  const ChatBubble({
    Key? key,
    required this.message,
    this.onQuickReplyTap,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;
    final isUser = message.sender == MessageSender.user;

    return Padding(
      padding: EdgeInsets.symmetric(
        horizontal: AppDimensions.screenPaddingHorizontal,
        vertical: AppDimensions.xs,
      ),
      child: Row(
        mainAxisAlignment:
            isUser ? MainAxisAlignment.end : MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (!isUser) ...[
            Container(
              width: 32.w,
              height: 32.h,
              decoration: BoxDecoration(
                color: isDark ? AppColors.darkSurface : AppColors.lightSurface,
                borderRadius: BorderRadius.circular(AppDimensions.radiusS),
              ),
              child: Icon(
                Icons.psychology,
                size: 18.sp,
                color: isDark ? AppColors.darkTextPrimary : AppColors.lightTextPrimary,
              ),
            ),
            SizedBox(width: AppDimensions.xs),
          ],
          Flexible(
            child: Column(
              crossAxisAlignment:
                  isUser ? CrossAxisAlignment.end : CrossAxisAlignment.start,
              children: [
                Container(
                  padding: EdgeInsets.all(AppDimensions.m),
                  decoration: BoxDecoration(
                    color: isUser
                        ? AppColors.black
                        : (isDark
                            ? AppColors.darkSurface
                            : AppColors.lightSurface),
                    borderRadius: BorderRadius.circular(AppDimensions.radiusL),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        message.text,
                        style: theme.textTheme.bodyLarge?.copyWith(
                          color: isUser
                              ? AppColors.white
                              : (isDark
                                  ? AppColors.darkTextPrimary
                                  : AppColors.lightTextPrimary),
                          fontSize: 14.sp,
                        ),
                      ),
                      if (message.bulletPoints != null &&
                          message.bulletPoints!.isNotEmpty) ...[
                        SizedBox(height: AppDimensions.s),
                        ...message.bulletPoints!.asMap().entries.map((entry) => Padding(
                            padding: EdgeInsets.only(bottom: AppDimensions.xs),
                            child: Row(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  '${entry.key + 1}. ',
                                  style: theme.textTheme.bodyLarge?.copyWith(
                                    color: isUser
                                        ? AppColors.white
                                        : (isDark
                                            ? AppColors.darkTextPrimary
                                            : AppColors.lightTextPrimary),
                                    fontSize: 14.sp,
                                    fontWeight: FontWeight.w500,
                                  ),
                                ),
                                Expanded(
                                  child: Text(
                                    entry.value,
                                    style: theme.textTheme.bodyLarge?.copyWith(
                                      color: isUser
                                          ? AppColors.white
                                          : (isDark
                                              ? AppColors.darkTextPrimary
                                              : AppColors.lightTextPrimary),
                                      fontSize: 14.sp,
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ],
                    ],
                  ),
                ),
                if (message.quickReplies != null &&
                    message.quickReplies!.isNotEmpty) ...[
                  SizedBox(height: AppDimensions.s),
                  Wrap(
                    spacing: AppDimensions.s,
                    runSpacing: AppDimensions.s,
                    children: message.quickReplies!
                        .map((reply) => QuickReplyChip(
                              label: reply,
                              onTap: () => onQuickReplyTap?.call(reply),
                            ))
                        .toList(),
                  ),
                ],
              ],
            ),
          ),
        ],
      ),
    );
  }
}

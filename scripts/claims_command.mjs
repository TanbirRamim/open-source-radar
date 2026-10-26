// Shared matcher for the self-serve /claim and /unclaim commands.
//
// The command can sit on any line ("hi, I'd like this one\n/claim"), and may
// follow leading @mentions ("@maintainer /claim"), but not inside a quote. Kept
// in one place so the claims workflow and its test always exercise the same code.
export const findCommand = (text) => {
  let inCodeFence = false;

  for (const rawLine of text.split("\n")) {
    const line = rawLine.trim();

    // Detect opening and closing code fences
    if (line.startsWith("```")) {
      inCodeFence = !inCodeFence;
      continue;
    }

    // Ignore commands inside code blocks
    if (inCodeFence) continue;

    // Remove leading mentions
    const command = line.replace(/^(@[\w-]+[\s,:]*)+/, "");

    // Find valid claim or unclaim command
    if (
      command.startsWith("/claim") ||
      command.startsWith("/unclaim")
    ) {
      return command;
    }
  }

  return undefined;
};

export const isStale = (times, now, days) => Math.max(0, ...times) <= now - days * 86400e3;

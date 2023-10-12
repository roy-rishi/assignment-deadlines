set assignments to {}

tell application "Google Chrome"
	repeat with t in tabs of window 1
		-- store list of [DUE DATE, SUBMISSION DATE, ASSN NAME]
		set assnInfo to {}

		-- record due dates
		tell t to set dueDate to execute javascript "document.querySelector('.assignment-details .due-date').innerHTML"
		set end of assnInfo to dueDate
		
		-- record submission dates
		tell t to set submissionDate to execute javascript "document.querySelector('.dropbox-revisions li.first').getAttribute('original-title')"
		set end of assnInfo to submissionDate

        -- record assignment name
        tell t to set assnName to the title of t
		set end of assnInfo to assnName

		set end of assignments to assnInfo
	end repeat
end tell

-- display data as python-formatted list of dictionary
log "["
repeat with i from 1 to length of assignments
    set assn to item i of assignments
    log "    {"
    log "        \"due\": \"" & item 1 of assn & "\","
    log "        \"sub\": \"" & item 2 of assn & "\","
    log "        \"name\": \"" & item 3 of assn & "\""
    if i is length of assignments then
        log "    }"
    else
        log "    },"
    end if
end repeat
log "]"

log "\n" & (length of assignments) & " tabs recorded"

-- return assignments
